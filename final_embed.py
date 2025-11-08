# updated_embeddings_pipeline.py
import os
import json
import time
import math
import requests
import numpy as np
import re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

CHUNK_SIZE = 800
OVERLAP = 0.25          # fraction overlap (25%)
MIN_CHUNK_SIZE = 50
EMBEDDINGS_DIR = "embeddings"
PROCESSED_DIR = "processed_documents"
MODEL = "nomic-embed-text:latest"
OLLAMA_URL = "http://localhost:11434"
MAX_WORKERS = 8         # tune to your CPU / Ollama capacity
REQUEST_TIMEOUT = 30

def preprocess_text(text: str) -> str:
    # Remove YAML frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL | re.MULTILINE)
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def extract_yaml_frontmatter(text: str) -> str:
    match = re.match(r'^(---\n.*?\n---\n)', text, flags=re.DOTALL)
    return match.group(1) if match else ''

def chunk_text_semantic(text: str, chunk_size: int = CHUNK_SIZE, overlap: float = OVERLAP) -> list:
    """
    Paragraph-aware chunking with configurable overlap.
    Overlap is applied by carrying last `overlap_chars` characters from previous chunk.
    """
    frontmatter = extract_yaml_frontmatter(text)
    if frontmatter:
        text_wo_frontmatter = text[len(frontmatter):]
    else:
        text_wo_frontmatter = text

    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text_wo_frontmatter) if p.strip()]
    chunks = []
    current_chunk = frontmatter if frontmatter else ""
    current_len = len(current_chunk)
    overlap_chars = int(chunk_size * overlap)

    for para in paragraphs:
        # if adding paragraph keeps size under limit, append
        if current_len + len(para) + 2 <= chunk_size or not current_chunk:
            current_chunk = (current_chunk + "\n\n" + para).strip() if current_chunk else para
            current_len = len(current_chunk)
        else:
            # finalize chunk
            if len(current_chunk.strip()) >= MIN_CHUNK_SIZE:
                chunks.append(current_chunk.strip())
            # start new chunk starting from the last `overlap_chars` of current_chunk + para
            tail = current_chunk[-overlap_chars:] if overlap_chars > 0 and len(current_chunk) > overlap_chars else ""
            current_chunk = (tail + "\n\n" + para).strip() if tail else para
            current_len = len(current_chunk)
    # last chunk
    if current_chunk and len(current_chunk.strip()) >= MIN_CHUNK_SIZE:
        chunks.append(current_chunk.strip())
    return chunks

def generate_embedding_ollama(text: str, model: str = MODEL, url: str = OLLAMA_URL, retries: int = 3, backoff: float = 0.5):
    """
    Generate embedding by calling local Ollama HTTP API.
    Returns list[float] or None on failure.
    """
    payload = {"model": model, "prompt": text}
    headers = {"Content-Type": "application/json"}
    for attempt in range(retries):
        try:
            resp = requests.post(f"{url}/api/embeddings", json=payload, timeout=REQUEST_TIMEOUT, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            # Ollama typically returns {"embedding": [...]}
            emb = data.get("embedding") or data.get("embeddings") or data.get("data", {}).get("embedding")
            if emb:
                return emb
            else:
                # fallback: some versions return 'data' array
                if "data" in data and isinstance(data["data"], list) and len(data["data"])>0:
                    # try common shapes
                    first = data["data"][0]
                    if isinstance(first, dict) and "embedding" in first:
                        return first["embedding"]
            # if we get here, unexpected response
            print("Unexpected embedding response:", data)
            return None
        except Exception as e:
            wait = backoff * (2 ** attempt)
            print(f"Embedding call failed (attempt {attempt+1}/{retries}): {e}. retry in {wait:.1f}s")
            time.sleep(wait)
    return None

def process_file(file_path: str, use_preprocess: bool = True, parallel_chunk_workers: int = 4):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if use_preprocess:
        text = preprocess_text(text)
    source_url = None
    # extract source_url from YAML frontmatter (simple)
    m = re.search(r'source_url:\s*["\']([^"\']+)["\']', text)
    if m:
        source_url = m.group(1)

    chunks = chunk_text_semantic(text)
    results = []
    # parallelize chunk embedding generation
    with ThreadPoolExecutor(max_workers=parallel_chunk_workers) as exe:
        futures = {exe.submit(generate_embedding_ollama, chunk): chunk for chunk in chunks}
        for future in as_completed(futures):
            chunk = futures[future]
            emb = future.result()
            if emb:
                results.append((chunk, emb))
    return {
        'file_path': file_path,
        'embeddings': [r[1] for r in results],
        'texts': [r[0] for r in results],
        'source_urls': [source_url]*len(results)
    }

def main():
    os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
    all_embeddings = []
    all_texts = []
    file_indices = []
    chunk_indices = []
    file_paths = []
    all_source_urls = []
    idx = 0

    for subdir in ['discourse', 'tds_course']:
        folder = Path(PROCESSED_DIR)/subdir
        if not folder.exists():
            continue
        md_files = list(folder.glob('*.md'))
        for mdfile in tqdm(md_files, desc=f"Processing {subdir}"):
            result = process_file(str(mdfile), parallel_chunk_workers=4)
            for i, emb in enumerate(result['embeddings']):
                all_embeddings.append(np.array(emb, dtype=np.float32))
                all_texts.append(result['texts'][i])
                file_indices.append(idx)
                chunk_indices.append(i)
                file_paths.append(str(mdfile))
                all_source_urls.append(result['source_urls'][i])
            idx += 1

    # Option A: save as npz (backwards compatible)
    np.savez_compressed(
        os.path.join(EMBEDDINGS_DIR, 'all_embeddings'),
        embeddings=np.vstack(all_embeddings) if len(all_embeddings) else np.zeros((0,)),
        texts=np.array(all_texts, dtype=object),
        file_indices=np.array(file_indices),
        chunk_indices=np.array(chunk_indices),
        file_paths=np.array(file_paths, dtype=object),
        source_urls=np.array(all_source_urls, dtype=object)
    )
    print(f"Saved {len(all_embeddings)} embeddings to {EMBEDDINGS_DIR}/all_embeddings.npz")

if __name__ == "__main__":
    main()
