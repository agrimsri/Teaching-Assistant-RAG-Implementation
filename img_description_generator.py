import os
import re
import json
import requests
import tempfile
from pathlib import Path
from typing import List, Dict, Tuple
import time
from urllib.parse import urlparse
from google import genai
from PIL import Image
import io
from dotenv import load_dotenv
load_dotenv()

class MarkdownImageProcessor:
    def __init__(self, api_keys: List[str], chunk_size: int = 1000, chunk_overlap: int = 100):
        """
        Initialize the processor with Gemini API keys (for rotation) and chunking parameters.
        """
        self.api_keys = api_keys
        self.current_key_index = 0
        self.client = genai.Client(api_key=self.api_keys[self.current_key_index])
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    # ===========================
    # API KEY ROTATION HANDLER
    # ===========================
    def rotate_key(self):
        """Rotate to the next API key."""
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        new_key = self.api_keys[self.current_key_index]
        self.client = genai.Client(api_key=new_key)
        print(f"[INFO] Switched to API Key #{self.current_key_index + 1}")

    # (Other functions like extract_images_from_markdown, download_image, etc. remain the same)

    def extract_images_from_markdown(self, content: str) -> List[Tuple[str, str]]:
        """
        Extract image URLs and their alt text from markdown content.
        
        Returns:
            List of tuples: (alt_text, image_url)
        """
        # Pattern to match ![alt](url) format
        pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
        matches = re.findall(pattern, content)
        return matches

    def generate_image_description(self, image_path: str, context: str = "") -> str:
        """
        Generate description for image using Gemini API, with key rotation on failure.
        """
        prompt = f"""Analyze this image and provide a detailed description that would be useful for search and understanding. 
Context: {context if context else 'This image is from an educational document.'}
Please describe:
1. What the image shows (charts, diagrams, screenshots, etc.)
2. Key elements, text, or data visible
3. The purpose or educational value
4. Any specific technical details
Keep the description factual and comprehensive."""

        attempts = 0
        while attempts < len(self.api_keys):
            try:
                my_file = self.client.files.upload(file=image_path)
                response = self.client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=[my_file, prompt],
                )
                try:
                    self.client.files.delete(my_file.name)
                except:
                    pass
                return response.text.strip()

            except Exception as e:
                print(f"[ERROR] {e} — rotating key...")
                self.rotate_key()
                attempts += 1
                time.sleep(2)

        return "[Image description unavailable after multiple API key attempts.]"

    # ===========================
    # PROGRESS TRACKING SYSTEM
    # ===========================
    def load_progress(self, progress_path: str) -> Dict[str, List[str]]:
        """Load progress from JSON file if exists."""
        if os.path.exists(progress_path):
            with open(progress_path, "r") as f:
                return json.load(f)
        return {}


    def save_progress(self, progress_path: str, progress_data: Dict[str, List[str]]):
        """Save current progress to JSON file."""
        with open(progress_path, "w") as f:
            json.dump(progress_data, f, indent=2)


    def create_text_chunks(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks for better embedding.
        
        Args:
            text: Input text to chunk
            
        Returns:
            List of text chunks
        """
        if len(text) <= self.chunk_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + self.chunk_size
            
            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence endings
                sentence_end = text.rfind('.', start, end)
                if sentence_end == -1:
                    sentence_end = text.rfind('!', start, end)
                if sentence_end == -1:
                    sentence_end = text.rfind('?', start, end)
                if sentence_end == -1:
                    # Look for paragraph breaks
                    sentence_end = text.rfind('\n\n', start, end)
                if sentence_end == -1:
                    # Look for any line break
                    sentence_end = text.rfind('\n', start, end)
                
                if sentence_end != -1 and sentence_end > start:
                    end = sentence_end + 1
            
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            # Move start position with overlap
            start = max(start + 1, end - self.chunk_overlap)
            
            if start >= len(text):
                break
        
        return chunks


    def download_image(self, url: str) -> str:
        """
        Download image from URL to temporary file.
        
        Returns:
            Path to temporary file
        """
        try:
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Get file extension from URL or content type
            parsed_url = urlparse(url)
            ext = os.path.splitext(parsed_url.path)[1]
            if not ext:
                content_type = response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    ext = '.jpg'
                elif 'png' in content_type:
                    ext = '.png'
                elif 'gif' in content_type:
                    ext = '.gif'
                elif 'webp' in content_type:
                    ext = '.webp'
                else:
                    ext = '.jpg'  # default
            
            # Create temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
            for chunk in response.iter_content(chunk_size=8192):
                temp_file.write(chunk)
            temp_file.close()
            
            return temp_file.name
            
        except Exception as e:
            print(f"Error downloading image {url}: {e}")
            return None


    def convert_image_to_webp(self, image_path: str) -> str:
        """
        Convert image to WebP format.
        
        Args:
            image_path: Path to the original image file
            
        Returns:
            Path to the converted WebP file
        """
        try:
            # Open the original image
            with Image.open(image_path) as img:
                # Convert image to RGB mode if not already in that mode
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as WebP format
                webp_path = f"{os.path.splitext(image_path)[0]}.webp"
                img.save(webp_path, 'webp')
                
            return webp_path
            
        except Exception as e:
            print(f"Error converting image to WebP {image_path}: {e}")
            return image_path  # Return original path on error

  
    def convert_webp_to_png(self, webp_path: str) -> str:
        """
        Convert WebP image to PNG format.
        
        Args:
            webp_path: Path to the WebP image file
            
        Returns:
            Path to the converted PNG file
        """
        try:
            # Open the WebP image
            with Image.open(webp_path) as img:
                # Create a new temporary file for PNG
                png_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
                png_path = png_file.name
                png_file.close()
                
                # Convert and save as PNG
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGBA', img.size, (255, 255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    background.convert('RGB').save(png_path, 'PNG')
                else:
                    img.convert('RGB').save(png_path, 'PNG')
                
                return png_path
        except Exception as e:
            print(f"Error converting WebP to PNG: {e}")
            return None
        

    def process_markdown_file(self, file_path: str, output_dir: str = None) -> Dict:
        """
        Process a single markdown file: extract images, generate descriptions, create chunks.
        """
        print(f"Processing: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract images
        images = self.extract_images_from_markdown(content)
        print(f"Found {len(images)} images")

        processed_content = content
        image_descriptions = {}

        for alt_text, image_url in images:
            print(f"Processing image: {image_url}")

            temp_image_path = self.download_image(image_url)
            if not temp_image_path:
                continue

            try:
                # If WebP, convert to PNG
                if temp_image_path.lower().endswith('.webp'):
                    png_path = self.convert_webp_to_png(temp_image_path)
                    if png_path:
                        try:
                            os.unlink(temp_image_path)
                        except:
                            pass
                        temp_image_path = png_path

                # Generate description (with key rotation built-in)
                description = self.generate_image_description(
                    temp_image_path,
                    context=f"Alt text: {alt_text}" if alt_text else ""
                )

                image_descriptions[image_url] = description

                # Replace original markdown image with description
                new_text = f"""**[Image Description]**: {description}

*Original image: ![{alt_text}]({image_url})*"""

                processed_content = processed_content.replace(
                    f"![{alt_text}]({image_url})",
                    new_text
                )

                print(f"Generated description for {image_url[:60]}...")

            finally:
                try:
                    os.unlink(temp_image_path)
                except:
                    pass

            time.sleep(1)  # Be gentle to API

        # Create text chunks
        chunks = self.create_text_chunks(processed_content)

        # Save processed markdown
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, os.path.basename(file_path))
        else:
            output_path = file_path

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)

        return {
            'file_path': file_path,
            'output_path': output_path,
            'images_processed': len(image_descriptions),
            'image_descriptions': image_descriptions,
            'chunks': chunks,
            'chunk_count': len(chunks)
        }


    def process_directory(self, input_dir: str, output_dir: str = None, progress_path: str = "progress.json") -> List[Dict]:
        """
        Process all markdown files in a directory with progress tracking.
        """
        print(f"Processing directory: {input_dir}")
        results = []

        # Load progress
        progress = self.load_progress(progress_path)
        processed_files = set(progress.get(input_dir, []))

        os.makedirs(output_dir, exist_ok=True)

        for file_path in Path(input_dir).glob("*.md"):
            file_name = os.path.basename(file_path)
            if file_name in processed_files:
                print(f"[SKIP] Already processed: {file_name}")
                continue

            try:
                result = self.process_markdown_file(str(file_path), output_dir)
                results.append(result)

                # Update progress after each successful file
                processed_files.add(file_name)
                progress[input_dir] = list(processed_files)
                self.save_progress(progress_path, progress)

            except KeyboardInterrupt:
                print("\n[INTERRUPTED] Saving progress and exiting safely...")
                progress[input_dir] = list(processed_files)
                self.save_progress(progress_path, progress)
                raise

            except Exception as e:
                print(f"[ERROR] Processing failed for {file_name}: {e}")
                results.append({'file_path': str(file_path), 'error': str(e)})
                # Save progress even after errors
                self.save_progress(progress_path, progress)

        return results


def main():
    # Configuration
    GOOGLE_API_KEY_1 = os.getenv("GOOGLE_API_KEY_1")
    GOOGLE_API_KEY_2 = os.getenv("GOOGLE_API_KEY_2")
    api_keys = [GOOGLE_API_KEY_1, GOOGLE_API_KEY_2]

    TDS_COURSE_DIR = "tds_course_md"
    DISCOURSE_DIR = "discourse_threads_md"
    OUTPUT_DIR = "processed_documents"
    PROGRESS_FILE = os.path.join(OUTPUT_DIR, "progress.json")

    processor = MarkdownImageProcessor(
        api_keys=api_keys,
        chunk_size=1000,
        chunk_overlap=100
    )

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = []

    tds_output_dir = os.path.join(OUTPUT_DIR, "tds_course")
    discourse_output_dir = os.path.join(OUTPUT_DIR, "discourse")

    print("=" * 50)
    print("Processing TDS Course Documents")
    print("=" * 50)
    tds_results = processor.process_directory(TDS_COURSE_DIR, tds_output_dir, PROGRESS_FILE)
    all_results.extend(tds_results)

    print("=" * 50)
    print("Processing Discourse Documents")
    print("=" * 50)
    discourse_results = processor.process_directory(DISCOURSE_DIR, discourse_output_dir, PROGRESS_FILE)
    all_results.extend(discourse_results)

    # Summary
    summary = {
        'total_files_processed': len(all_results),
        'total_images_processed': sum(r.get('images_processed', 0) for r in all_results),
        'total_chunks_created': sum(r.get('chunk_count', 0) for r in all_results),
        'files': all_results
    }

    with open(os.path.join(OUTPUT_DIR, "processing_summary.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    print("=" * 50)
    print("PROCESSING COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()
