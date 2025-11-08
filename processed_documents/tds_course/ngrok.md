---
source_url: "https://tds.s-anand.net/#/ngrok"
---

## Tunneling: ngrok

[Ngrok](https://ngrok.com/) is a tool that creates secure tunnels to your localhost, making your local development server accessible to the internet. It's essential for testing webhooks, sharing work in progress, or debugging applications in production-like environments.

Run the command `uvx ngrok http 8000` to create a tunnel to your local server on port 8000. This generates a public URL that you can share with others.

To get started, log into `ngrok.com` and [get an authtoken from the dashboard](https://dashboard.ngrok.com/get-started/your-authtoken). Copy it. Then run:

```bash
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

Now you can forward any local port to the internet. For example:

```bash
# Start a local server on port 8000
uv run -m http.server 8000

# Start HTTP tunnel
uvx ngrok http 8000
```

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Description:**

The image appears to be a screenshot of a tutorial or demonstration about ngrok. There are three separate application windows visible. Central to the image is a dark background with white text overlay that states "NGROK In 60 seconds".

2.  **Key Elements, Text, or Data Visible:**
    *   **Application Windows:** There are what appears to be three different application windows open.
        *   **GitHub Interface:** On the left is a web interface of GitHub. It displays a repository named 'webfuse\_techlab'. There are navigation options like "Pull requests," "Issues," "Marketplace," and "Explore". A list of files and directories in the repository is displayed.
        *   **File Explorer:** In the upper-right, there is a file explorer. It shows a directory structure with files and folder names like "data," "_internal\_metadata," "scripts," etc.
        *   **Terminal:** The bottom-right displays a terminal. It shows some command-line output. Text within the terminal indicates information like: "Loading ngrok version 3.2.2.", "Update available 3.6.0.6". There is also a line that starts with "metrics: usage... "
    *   **Text Overlay:** The "NGROK In 60 seconds" text suggests a tutorial or a brief demonstration of ngrok.

3.  **Purpose and Educational Value:**

The purpose of the image is likely to promote or educate about ngrok. It seems to be part of a short tutorial that covers the basics. The GitHub interface and file explorer likely represent the context or setup of a project where ngrok might be useful. The terminal window probably demonstrates how to execute ngrok and the resulting output.

4.  **Specific Technical Details:**

*   **ngrok:** ngrok is a reverse proxy that creates secure tunnels from a public endpoint (e.g., the internet) to a locally running service. This allows developers to expose their local development environments without deploying them to a public server.
*   **Version Information:** The terminal output displays specific version numbers of ngrok (version 3.2.2 and an available update to version 3.6.0.6), which would be relevant for a technical tutorial.
*   **GitHub Repository:** The presence of a GitHub repository suggests a project or code base that ngrok can be integrated with.
*   **Lockbox** The presence of 'Lockbox' in the bottom left may indicate a tool or application relevant to this workflow.

In summary, the image is a thumbnail or a screen capture from an ngrok tutorial video. It uses elements like GitHub, file system views, and a terminal interface to indicate a real-world development scenario.

*Original image: ![ngrok in 60 seconds](https://i.ytimg.com/vi_webp/dfMdLGZLXSg/sddefault.webp)*](https://youtu.be/dfMdLGZLXSg)
