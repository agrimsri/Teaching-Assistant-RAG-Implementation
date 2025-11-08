---
source_url: "https://tds.s-anand.net/#/llamafile"
---

## Local LLMs: Llamafile

You would have heard of Large Language Models (LLMs) like GPT-4, Claude, and Llama. Some of these models are available for free, but most of them are not.

An easy way to run LLMs locally is Mozilla's [Llamafile](https://github.com/Mozilla-Ocho/llamafile). It's a single executable file that works on Windows, Mac, and Linux. No installation or configuration needed - just download and run.

Watch this Llamafile Tutorial (6 min):

[**[Image Description]**: Here's a detailed description of the image:

**1. Content and Visual Elements:**

*   **Main Visual:** The image prominently features a whimsical, cartoon-like depiction of a llama. The llama is rendered in grayscale with a sketched, textured effect.
*   **Supporting Graphics:** To the left of the llama, there is a sketch of a computer monitor displaying lines of code or text. Below the monitor, there's an abstract diagram resembling a simplified circuit board with interconnected circles and lines. To the upper right of the llama, a sketched gear/cog is present.
*   **Text:** To the right of the llama, in a bold, reddish-brown font, is the word "Llamafile". Below "Llamafile" in a smaller font and the same reddish-brown color, the phrase "Local LLMs Made Easy" is written.

**2. Key Elements, Text, and Data:**

*   **Llama:** Serves as a mascot or visual representation, connecting to the name "Llamafile."
*   **Computer/Code:** Illustrates the computational or software-related aspect of the product.
*   **Circuit Diagram:** Likely symbolizes the underlying technology or connectivity involved.
*   **Gear/Cog:** Symbolizes mechanism or settings.
*   **"Llamafile":** The name of the product, likely software or a tool.
*   **"Local LLMs Made Easy":** A tagline explaining the product's core functionality. LLMs stand for Large Language Models.

**3. Purpose and Educational Value:**

*   **Product Promotion:** The image is designed to promote "Llamafile," a product or tool.
*   **Simplified Explanation:** The tagline "Local LLMs Made Easy" suggests the product aims to make complex machine learning models (LLMs) accessible and easy to use on local machines.
*   **Target Audience:** The friendly, cartoonish style might appeal to developers, researchers, or anyone interested in exploring LLMs.

**4. Technical Details (Implied):**

*   **Local LLMs:** Indicates that the product allows running LLMs on a user's own computer rather than relying on cloud-based services. This could imply features for model management, optimization, or inference on local hardware.
*   **Ease of Use:** The "Made Easy" aspect suggests a user-friendly interface or simplified workflow for working with LLMs.

**Overall:** The image serves as a visual introduction to "Llamafile," emphasizing its focus on making Local Large Language Models more accessible and easier to implement.

*Original image: ![Llamafile: Local LLMs Made Easy](https://img.youtube.com/vi/d1Fnfvat6nM/0.jpg)*](https://youtu.be/d1Fnfvat6nM)

Here's how to get started

1. [Download `Llama-3.2-1B-Instruct.Q6_K.llamafile` (1.11 GB)](https://huggingface.co/Mozilla/Llama-3.2-1B-Instruct-llamafile/blob/main/Llama-3.2-1B-Instruct.Q6_K.llamafile?download=true).
2. From the command prompt or terminal, run `Llama-3.2-1B-Instruct.Q6_K.llamafile`.
3. Optional: For GPU acceleration, use `Llama-3.2-1B-Instruct.Q6_K.llamafile --n-gpu-layers 35`. (Increase or decrease the number of layers based on your GPU VRAM.)

You might see a message like this:

```text
██╗     ██╗      █████╗ ███╗   ███╗ █████╗ ███████╗██╗██╗     ███████╗
██║     ██║     ██╔══██╗████╗ ████║██╔══██╗██╔════╝██║██║     ██╔════╝
██║     ██║     ███████║██╔████╔██║███████║█████╗  ██║██║     █████╗
██║     ██║     ██╔══██║██║╚██╔╝██║██╔══██║██╔══╝  ██║██║     ██╔══╝
███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║     ██║███████╗███████╗
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
software: llamafile 0.8.17
model:    Llama-3.2-1B-Instruct-Q8_0.gguf
compute:  13th Gen Intel Core i9-13900HX (alderlake)
server:   http://127.0.0.1:8080/

A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
```

You can now chat with the model. Type `/exit` or press `Ctrl+C` to stop.

You can also visit `http://127.0.0.1:8080/` in your browser to chat with the model.

LlamaFile exposes an OpenAI compatible API. Here's how to use it in Python:

```python
import requests

response = requests.post(
    "http://localhost:8080/v1/chat/completions",
    headers={"Content-Type": "application/json"},
    json={"messages": [{"role": "user", "content": "Write a haiku about coding"}]}
)
print(response.json()["choices"][0]["message"]["content"])
```

Tools:

- [OpenAI API compatibility](https://platform.openai.com/docs/api-reference/chat): Use existing OpenAI code
- [Creating your own llamafiles](https://github.com/Mozilla-Ocho/llamafile#creating-llamafiles): Control output format
