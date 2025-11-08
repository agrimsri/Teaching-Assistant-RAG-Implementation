---
source_url: "https://tds.s-anand.net/#/docker"
---

## Containers: Docker, Podman

[Docker](https://www.docker.com/) and [Podman](https://podman.io/) are containerization tools that package your application and its dependencies into a standardized unit for software development and deployment.

Docker is the industry standard. Podman is compatible with Docker and has better security (and a slightly more open license). In this course, we recommend Podman but Docker works in the same way.

Initialize the container engine:

```bash
podman machine init
podman machine start
```

Common Operations. (You can use `docker` instead of `podman` in the same way.)

```bash
# Pull an image
podman pull python:3.11-slim

# Run a container
podman run -it python:3.11-slim

# List containers
podman ps -a

# Stop container
podman stop container_id

# Scan image for vulnerabilities
podman scan myapp:latest

# Remove container
podman rm container_id

# Remove all stopped containers
podman container prune
```

You can create a `Dockerfile` to build a container image. Here's a sample `Dockerfile` that converts a Python script into a container image.

```dockerfile
FROM python:3.11-slim
# Set working directory
WORKDIR /app
# Typically, you would use `COPY . .` to copy files from the host machine,
# but here we're just using a simple script.
RUN echo 'print("Hello, world!")' > app.py
# Run the script
CMD ["python", "app.py"]
```

To build, run, and deploy the container, run these commands:

```bash
# Create an account on https://hub.docker.com/ and then login
podman login docker.io

# Build and run the container
podman build -t py-hello .
podman run -it py-hello

# Push the container to Docker Hub. Replace $DOCKER_HUB_USERNAME with your Docker Hub username.
podman push py-hello:latest docker.io/$DOCKER_HUB_USERNAME/py-hello

# Push adding a specific tag, e.g. dev
TAG=dev podman push py-hello docker.io/$DOCKER_HUB_USERNAME/py-hello:$TAG
```

Tools:

- [Dive](https://github.com/wagoodman/dive): Explore image layers
- [Skopeo](https://github.com/containers/skopeo): Work with container images
- [Trivy](https://github.com/aquasecurity/trivy): Security scanner

[**[Image Description]**: Here's a detailed description of the image:

1.  **What the image shows:** The image appears to be a thumbnail for a video tutorial or online course about Podman. It is split into two sections. The left side has a purple background with text and a logo. The right side shows a man giving a presentation.

2.  **Key elements, text, or data visible:**
    *   **Text on the left side:**
        *   "Giuseppe Scaramuzzino" (likely the name of the instructor or presenter)
        *   "Podman tutorial: from zero to hero" (the title of the tutorial)
        *   "Full Course in 1 Hour"
        *   "AMADEUS" (a logo or branding element)
    *   **Logo:** There's a small logo showing three cartoon seals in a hexagonal frame.
    *   **Right Side:**
        *   A man with glasses is holding a microphone and gesturing with his right hand. He is wearing a black t-shirt and a lanyard with a badge.
        *   The background is blurred and seems to be a stage with a screen or backdrop featuring the text "Lead".
        *   The text "Lead" is partially visible in the background.

3.  **The purpose or educational value:** The image promotes a comprehensive tutorial on Podman, aimed at taking users from beginner ("zero") to proficient ("hero") level in one hour.

4.  **Any specific technical details:**
    *   The tutorial focuses on Podman, which is a container management tool similar to Docker but without requiring a daemon.
    *   The title "from zero to hero" suggests a beginner-friendly introduction to the topic.
    *   The "Full Course in 1 Hour" duration is mentioned, indicating a concise and time-efficient learning experience.

*Original image: ![Podman Tutorial Zero to Hero | Full 1 Hour Course](https://i.ytimg.com/vi_webp/YXfA5O5Mr18/sddefault.webp)*](https://youtu.be/YXfA5O5Mr18)

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a thumbnail from a YouTube video. It's a graphical slide designed to attract viewers, blending text and stylized graphics.

2.  **Key Elements, Text, or Data Visible:**
    *   **Title:** The primary text reads "HOW TO DOCKERIZE IN 7 EASY STEPS". "DOCKERIZE" is larger and more prominent.
    *   **Docker Symbol:** A blue whale icon with container boxes on its back, which is a recognized symbol of Docker, is integrated into the "DOCKERIZE" text, replacing the "D".
    *   **"7":** The number 7 is represented by seven steps or lines.
    *   **"EASY" and "STEPS":** These words appear in separate green boxes.
    *   **Node.js Logo:** A circular logo with the Node.js icon is placed on the upper right. It contains the text "nodeJS" and a flame with the text "3.3".
    *   **Background:** The background is split diagonally, with a blue color on the left and a gradient green on the right side.

3.  **Purpose and Educational Value:** The image is designed to entice viewers to watch a tutorial on how to use Docker, specifically within a Node.js context. The "7 Easy Steps" promises a simplified approach to learning Docker, appealing to beginners.

4.  **Specific Technical Details:**
    *   **Docker:** Docker is a platform for containerization, a technology that allows you to package an application with all of its dependencies into a standardized unit for software development. The image promises to teach viewers how to use Docker.
    *   **Node.js:** A runtime environment for executing JavaScript code server-side.

**Summary:** The image is a YouTube thumbnail promoting a beginner-friendly tutorial on Dockerizing Node.js applications in 7 easy steps. The design uses familiar symbols and clear text to quickly communicate the video's topic.

*Original image: ![Learn Docker in 7 Easy Steps - Full Beginner's Tutorial](https://i.ytimg.com/vi_webp/gAkwW2tuIqE/sddefault.webp)*](https://youtu.be/gAkwW2tuIqE)

- Optional: For Windows, see [WSL 2 with Docker getting started](https://youtu.be/5RQbdMn04Oc)
