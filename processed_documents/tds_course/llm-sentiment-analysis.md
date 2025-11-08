---
source_url: "https://tds.s-anand.net/#/llm-sentiment-analysis"
---

## LLM Sentiment Analysis

[OpenAI's API](https://platform.openai.com/) provides access to language models like GPT 4o, GPT 4o mini, etc.

For more details, read OpenAI's guide for:

- [Text Generation](https://platform.openai.com/docs/guides/text-generation)
- [Vision](https://platform.openai.com/docs/guides/vision)
- [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Start with this quick tutorial:

[**[Image Description]**: Here's a detailed description of the image, broken down into key elements:

**1. What the Image Shows**

The image is a screenshot of a code editor, likely VS Code, displaying the contents of a `.zshrc` file. This file is commonly used in macOS and Linux systems to configure the Zsh shell environment. The code snippet shows a series of environment variables being set and some shell configurations.

**2. Key Elements, Text, and Data Visible**

*   **File:** `.zshrc` (Z shell resource file)
*   **Code:** The code consists of several lines setting environment variables. Key lines include:
    *   `export PATH="/opt/homebrew/opt/ruby/bin:$PATH"`:  Adds a Ruby directory to the PATH environment variable.
    *   `export LANG=en_US.UTF-8`, `export LANGUAGE=en_US.UTF-8`, `export LC_ALL=en_US.UTF-8`: Sets language and locale settings.
    *   `export ANDROID_HOME=$HOME/Library/Android/sdk`: Sets the path to the Android SDK.
    *   `export PATH=$PATH:$ANDROID_HOME/emulator` and `export PATH=$PATH:$ANDROID_HOME/platform-tool`: Appends the emulator and platform-tools directories to the PATH variable, likely for Android development.
    *   `export PATH=/usr/local/bin:$PATH`: Adds the `/usr/local/bin` directory to the PATH.
    *   `export OPENAI_API_KEY='sk-proj-qZIGbilFyPY'`: Sets the OpenAI API key as an environment variable. This line is particularly significant.
    *   `source <(ng completion script)`:  Loads Angular CLI autocompletion.
    *   `eval "$(~/.local/bin/mise activate zsh)"`: This line executes a command to activate the Zsh shell, which likely relates to an environment manager.
*   **File Information:** The file appears to be associated with the user "amosgyamfi." There's also a comment indicating that the PATH modifications were made by "pipx" on "2024-04-22 10:33:04."
*   **Text in Editor:** There is additional text, not directly part of the code, which gives information about the editor settings (e.g., "Shell Script," "Prettier") and some status indicators.
*   **Filename:** The filename is ".zshrc" which is a configuration file for the Zsh shell.
*   **User Path:** The user's path is shown as "Users > amosgyamfi".
*   **API Key:** The OpenAI API Key is 'sk-proj-qZIGbilFyPY'.

**3. The Purpose or Educational Value**

*   **Environment Configuration:** The file serves to configure the shell environment for a user. This is a common practice to streamline development workflows by making tools and SDKs accessible from the command line.
*   **Setting Environment Variables:** The example demonstrates how to set environment variables, specifically `PATH`, `ANDROID_HOME` and `OPENAI_API_KEY`.
*   **Developer Workflow:** It gives a glimpse into the setup process for a developer who might be working with Android development, Angular CLI, and OpenAI's API.
*   **Configuration Management:** The comments about "pipx" show how automated tools might be used to manage environment configurations.
*   **Security Considerations:** The image highlights a potential security concern: hardcoding an API key (in this case, an OpenAI API key) directly in a configuration file.  It's generally recommended to use more secure methods for handling API keys, such as environment variables loaded from a more secure location or configuration management tools.

**4. Specific Technical Details**

*   **Zsh Shell:** The image relates specifically to the Zsh shell, a popular alternative to Bash.
*   **PATH Variable:** The PATH variable is a crucial environment variable that tells the shell where to look for executable files.
*   **Homebrew and Android SDK:** The inclusion of Homebrew and Android SDK paths indicates the developer is using these tools.
*   **pipx:**  `pipx` is a tool for installing and running Python applications in isolated environments.
*   **Angular CLI:** The `ng completion script` suggests the developer is working with Angular, a JavaScript framework for building web applications.
*  **Mise:** Mise (previously called rtx) is an open source tool to manage versions of programming language runtimes and tools.

In summary, the image presents a configuration file for a Zsh shell, showcasing how environment variables are set for development purposes. It hints at a workflow involving Android development, Angular CLI, and potentially OpenAI API usage. It also demonstrates the potential risk of hardcoding API keys.

*Original image: ![OpenAI API Quickstart: Send your First API Request](https://i.ytimg.com/vi_webp/Xz4ORA0cOwQ/sddefault.webp)*](https://youtu.be/Xz4ORA0cOwQ)

Here's a minimal example using `curl` to generate text:

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{ "role": "user", "content": "Write a haiku about programming." }]
  }'
```

Let's break down the request:

- `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
- `-H "Content-Type: application/json"`: The content type of the request.
- `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
- `-d`: The request body.
  - `"model": "gpt-4o-mini"`: The model to use for text generation.
  - `"messages":`: The messages to send to the model.
    - `"role": "user"`: The role of the message.
    - `"content": "Write a haiku about programming."`: The content of the message.

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image is a screenshot of what appears to be a videoconference call, likely a work or educational session. A window showing code or text is open on a computer, with a sidebar of the video conferencing interface showing the thumbnails of several participants.
2.  **Key elements, text, or data visible:**
    *   **Code/Text:** The main window shows formatted text or code in a dark theme, with sections highlighted in different colors. The text is about a place called "OZ," and the content seems to be describing a "Security State Penitentary," with an "experimental section of the prison where fronts and face inwards." It also mentions groups like "Aryans, Muslims, gangsters, Italians, Irish" and that "scuffles and shady agreements are never far away".
    *   **Videoconference Participants:**
        *   Two video feeds are visible: one of a man named "Anand S" and another of a man named "Dibu John Philip."
        *   Two other participants are indicated by circular profile pictures, one named "prasanna" with the initial "P," and another named "Amit K. Gupta" with the initials "AG."
    *   **Interface Elements:**
        *   The window title seems to include "Untitled Copy.ipynb - Colab" implying a Google Colaboratory notebook. There are tabs labeled "Overview - OpenAI API" and "OpenAl Platform".
        *   The URL bar shows `https://platform.openai.com/tokenizer`.
3.  **The purpose or educational value:** The image seems to capture a session where code related to OpenAI is being discussed or worked on collaboratively. The text about "OZ" is likely a string that may be used for experimentation or sentiment analysis. The videoconference suggests a remote team working or learning together.
4.  **Specific technical details:** The screen is a snippet of a Jupyter Notebook interface (Colab), which is an interactive coding environment used for data analysis, machine learning, and education. The highlighted syntax suggests the potential use of the OpenAI API or related tokenizer for tasks involving natural language processing and machine learning.

*Original image: ![LLM Sentiment Analysis](https://i.ytimg.com/vi_webp/_D46QrX-2iU/sddefault.webp)*](https://youtu.be/_D46QrX-2iU)

This video explains how to use large language models (LLMs) for sentiment analysis and classification, covering:

- **Sentiment Analysis**: Use OpenAI API to identify the sentiment of movie reviews as positive or negative.
- **Prompt Engineering**: Learn how to craft effective prompts to get desired results from LLMs.
- **LLM Training**: Understand how to train LLMs by providing examples and feedback.
- **OpenAI API Integration**: Integrate OpenAI API into Python code to perform sentiment analysis.
- **Tokenization**: Learn about tokenization and its impact on LLM input and cost.
- **Zero-Shot, One-Shot, and Multi-Shot Learning**: Understand different approaches to using LLMs for learning.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1tVZBD9PKto1kPmVJFNUt0tdzT5EmLLWs)
- [Movie reviews dataset](https://drive.google.com/file/d/1X33ao8_PE17c3htkQ-1p2dmW2xKmOq8Q/view)
- [OpenAI Playground](https://platform.openai.com/playground/chat)
- [OpenAI Pricing](https://openai.com/api/pricing/)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference/)
- [OpenAI Docs](https://platform.openai.com/docs/overview)
