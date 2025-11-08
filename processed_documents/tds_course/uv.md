---
source_url: "https://tds.s-anand.net/#/uv"
---

## Python tools: uv

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager that's becoming the standard for running Python scripts. It replaces tools like pip, conda, pipx, poetry, pyenv, twine, and virtualenv into one, enabling:

- **Python Version Management**: uv installs and manages _multiple_ Python versions, allowing developers to specify and switch between versions seamlessly.
- **Virtual Environment Handling**: It automates the creation and management of virtual environments, ensuring isolated and consistent development spaces for different projects.
- **Dependency Management**: With support for the pyproject.toml format, uv enables precise specification of project dependencies. It maintains a universal lockfile, uv.lock, to ensure reproducible installations across different systems.
- **Project Execution**: The `uv run` command allows for the execution of scripts and applications within the managed environment, streamlining development workflows.

Here are some commonly used commands:

```bash
# Replace python with uv. This automatically installs Python and dependencies.
uv run script.py

# Run a Python script directly from the Internet
uv run https://example.com/script.py

# Run a Python script without installing
uvx ruff

# Use a specific Python version
uv run --python 3.11 script.py

# Add dependencies to your script
uv add httpx --script script.py

# Create a virtual environment at .venv
uv venv

# Install packages to your virtual environment
uv pip install httpx
```

uv uses [inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) for dependencies.
The eliminates the need for `requirements.txt` or virtual environments. For example:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
# ]
# ///
```

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a frame from a video or presentation introducing "uv," a Python package and project manager. The overall aesthetic is modern, with bright, gradient colors in the background. The image features a person in a black shirt pointing to elements on the screen.

2.  **Key Elements, Text, and Data:**
    *   **Text:**
        *   "ultra-fast Python package/project manager" is prominently displayed in bold white text within a rounded black rectangle.
        *   "uv" is shown in a larger, stylized font in purple, split between a rounded white rectangular shape and a partially obscured purple shape resembling a rotated "U."
    *   **Graphics:**
        *   A graphic representing the Python logo is present, suggesting the software is related to Python.
        *   An orange circle with a black bug or lightbulb graphic attached to the top corner is present.
    *   **Person:** A man is shown pointing with both hands towards different elements on the screen. He is likely the presenter or host of the video.

3.  **Purpose or Educational Value:** The image serves as a promotional thumbnail or title card for a video or presentation. Its purpose is to introduce and highlight "uv" as a fast Python package and project manager, which would be of interest to Python developers or software engineers. The visual elements aim to attract attention and convey the software's core function and speed.

4.  **Specific Technical Details:**
    *   The text "ultra-fast" suggests that the software offers performance improvements over existing Python package managers.
    *   The Python logo indicates the software is compatible with Python environments.
    *   The phrase "package/project manager" describes the software's primary function: managing dependencies and project structure.
    *   Inline Script Metadata (28 min) implies the content is a video that is approximately 28 minutes long.

*Original image: ![uv - Python package and project management | Inline Script Metadata (28 min)](https://i.ytimg.com/vi_webp/igWlYl3asKw/sddefault.webp)*](https://youtu.be/igWlYl3asKw?t=1240)

<!-- Assessment: Share output of `uv run --with httpie -- https https://httpbin.org/get?email={email}` -->
<!-- Assessment: Share output of `uvx markitdown {email}.pdf` -->
<!-- Assessment: Share output of `uv ruff format script.py` -->
