---
source_url: "https://tds.s-anand.net/#/vercel"
---

## Serverless hosting: Vercel

<!--

Why Vercel? I evaluated from https://survey.stackoverflow.co/2024/technology#2-cloud-platforms

- AWS, Azure, Google Cloud are too complex for beginners
- Cloudflare (next most popular, widely admired) Python support is in beta
- Hetzner (most admired), Supabase (next most admired) do not have a serverless platform
- Fly.io (next most admired) does not have a free tier
- Heroku (used in previous terms) is the least admired
- Vercel is both popular, admired, growing, has a free plan, and a simple API

-->

Serverless platforms let you rent a single function instead of an entire machine. They're perfect for small web tools that _don't need to run all the time_. Here are some common real-life uses:

- A contact form that emails you when someone wants to hire you (runs for 2-3 seconds, a few times per day)
- A tool that converts uploaded photos to black and white (runs for 5-10 seconds when someone uploads a photo)
- A chatbot that answers basic questions about your business hours (runs for 1-2 seconds per question)
- A newsletter sign-up that adds emails to your mailing list (runs for 1 second per sign-up)
- A webhook that posts your Etsy sales to Discord (runs for 1 second whenever you make a sale)

You only pay when someone uses your tool, and the platform automatically handles busy periods. For example, if 100 people fill out your contact form at once, the platform creates 100 temporary copies of your code to handle them all. When they're done, these copies disappear. It's cheaper than running a full-time server because you're not paying for the time when no one is using your tool - most tools are idle 95% of the time!

Rather than writing a full program, serverless platforms let you write functions. These functions are called via HTTP requests. They run in a cloud environment and are scaled up and down automatically. But this means you write programs in a different style. For example:

- You can't `pip install` packages - you have to use `requirements.txt`
- You can't read or write files from the file system - you can only use APIs.
- You can't run commands (e.g. `subprocess.run()`)

[Vercel](https://vercel.com/) is a cloud platform optimized for frontend frameworks and serverless functions. Vercel is tightly integrated with GitHub. Pushing to your repository automatically triggers new deployments.

Here's a [quickstart](https://vercel.com/docs/functions/runtimes/python). [Sign-up with Vercel](https://vercel.com/signup). Create an empty `git` repo with this `api/index.py` file.

To deploy a FastAPI app, add a `requirements.txt` file with `fastapi` as a dependency.

```text
fastapi
```

Add your FastAPI code to a file, e.g. `main.py`.

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

Add a `vercel.json` file to the root of your repository.

```json
{
  "builds": [{ "src": "main.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "main.py" }]
}
```

On the command line, run:

- `npx vercel` to deploy a test version
- `npx vercel --prod` to deploy to production

**Environment Variables**. Use `npx vercel env add` to add environment variables. In your code, use `os.environ.get('SECRET_KEY')` to access them.

### Videos

[**[Image Description]**: Here is a detailed description of the image:

1.  **Image Description:** The image is a screen capture from a video, featuring a man on the left side gesturing with two fingers, and the Vercel platform's interface on the right. The Vercel logo is prominently displayed in the center of the image, overlayed over the screen capture.

2.  **Key Elements and Text:**
    *   **Vercel Platform Interface:** The right side showcases the Vercel dashboard, including the Vercel logo, a "Git Provider" label, the organization name "Acme" marked as "Enterprise," and navigation tabs for "Projects," "Integrations," "Activity," "Domains," "Usage," and "Settings."
    *   **Dashboard Content:** Below the navigation, there's a search bar, a list of projects, including "vercel-times (verceltimes.com)." Under this project, there is a description "update img src From change-logo 2 min ago via (github icon)." Another update listed is "Updated docs on layout from [user name] 18 min ago via (github icon)"
    *   **Vercel Logo:** A white triangular logo of Vercel is prominent over the image, with the text "Vercel" written next to it.
    *   **Man:** A man is featured on the left side of the screen.

3.  **Purpose and Educational Value:** The image promotes the Vercel platform, showcasing its dashboard interface and providing a glimpse into project management and updates within the platform. The image is titled as a Vercel Product Walkthrough which means the video is probably a tutorial or product demonstration. It is designed to highlight the user-friendly interface and demonstrate features such as project management, integration with Git providers, and activity monitoring.

4.  **Technical Details:**
    *   The image is a screen capture of a digital interface.
    *   The platform is geared towards web development and deployment.
    *   Git integration and project management are key components of the Vercel platform.

*Original image: ![Vercel Product Walkthrough](https://i.ytimg.com/vi_webp/sPmat30SE4k/sddefault.webp)*](https://youtu.be/sPmat30SE4k)

[**[Image Description]**: Here's a detailed description of the image:

1.  **What the image shows:** The image is a thumbnail for a video tutorial, most likely on YouTube, showcasing how to deploy FastAPI (a Python web framework) on Vercel (a cloud platform). It features a man pointing towards the visual elements on the screen.

2.  **Key elements, text, or data visible:**
    *   **Text:** The prominent text "DEPLOY FAST" is displayed in large, white capital letters.
    *   **Visual Elements:**
        *   A thick, black triangle is positioned prominently on the left.
        *   Behind the triangle is a green circular logo with a white lightning bolt symbol in it, which strongly resembles the Vercel logo.
        *   The background features a faint pattern of binary code (1s and 0s), giving it a tech-oriented feel.
        *   A smiling man is visible on the right side of the image, pointing with his right hand toward the left. He is wearing a gray t-shirt.

3.  **Purpose or educational value:** The thumbnail aims to attract viewers interested in quickly and easily deploying FastAPI applications on Vercel. It implies a simple, efficient, and rapid deployment process. The "Deploy Fast" text emphasizes the speed and ease of the tutorial. The image serves as a visual advertisement for the video tutorial, conveying its subject matter at a glance.

4.  **Specific technical details:** The image suggests the following technical details:
    *   **FastAPI:** The tutorial is centered around the FastAPI framework, indicating it might cover topics like creating API endpoints, handling data, and leveraging FastAPI's built-in features.
    *   **Vercel:** The presence of the Vercel logo indicates the tutorial will guide users on how to deploy their FastAPI application on the Vercel platform, likely covering aspects like configuration, deployment steps, and potentially CI/CD integration.

In summary, the image is a visually engaging thumbnail designed to attract viewers interested in a tutorial on deploying FastAPI applications using the Vercel platform, emphasizing a fast and easy deployment process.

*Original image: ![Deploy FastAPI on Vercel | Quick and Easy Tutorial](https://i.ytimg.com/vi_webp/8R-cetf_sZ4/sddefault.webp)*](https://youtu.be/8R-cetf_sZ4)
