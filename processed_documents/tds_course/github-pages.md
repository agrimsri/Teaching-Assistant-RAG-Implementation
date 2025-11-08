---
source_url: "https://tds.s-anand.net/#/github-pages"
---

## Static hosting: GitHub Pages

[GitHub Pages](https://pages.github.com/) is a free hosting service that turns your GitHub repository directly into a whenever you push it. This is useful for sharing analysis results, data science portfolios, project documentation, and more.

Common Operations:

```bash
# Create a new GitHub repo
mkdir my-site
cd my-site
git init

# Add your static content
echo "<h1>My Site</h1>" > index.html

# Push to GitHub
git add .
git commit -m "feat(pages): initial commit"
git push origin main

# Enable GitHub Pages from the main branch on the repo settings page
```

Best Practices:

1. **Keep it small**
   - [Optimize images](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/Multimedia). Prefer SVG over WEBP over 8-bit PNG.
   - [Preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload) critical assets like stylesheets
   - Avoid committing large files like datasets, videos, etc. directly. Explore [Git LFS](https://git-lfs.github.com/) instead.

Tools:

- [GitHub Desktop](https://desktop.github.com/): GUI for Git operations
- [GitHub CLI](https://cli.github.com/): Command line interface
- [GitHub Actions](https://github.com/features/actions): Automation

[**[Image Description]**: Here's a detailed description of the image:

1.  **What the image shows:** The image is a combination of a screenshot and a person. On the left side, there is a screenshot of a GitHub Pages interface, likely from a computer screen. The right side features a woman in the frame, who appears to be looking directly at the viewer, and is likely a presenter in a video. Overlaid on the GitHub Pages interface are large, stylized words.

2.  **Key elements, text, or data visible:**
    *   **GitHub Pages:** The title "GitHub Pages" is prominently displayed, with a subtitle indicating it's designed for hosting personal and organizational websites.
    *   **Interface Elements:** There are snippets of interface elements visible, like "Source," with a dropdown menu set to "None," and a "Save" button. "Theme Chooser" is also visible.
    *   **Overlaid Text:** The words "Hosting websites" are placed over the screenshot in large, outlined text, likely indicating the topic of a video or presentation.
    *   **Person:** A woman with fair skin and dark hair, wearing a gray hooded sweatshirt and a necklace, is positioned on the right. She is smiling.

3.  **Purpose or educational value:**
    The image is likely used for an educational purpose, such as a tutorial or promotional material for GitHub Pages. It seems aimed at teaching or informing viewers how to host a website using GitHub Pages. The inclusion of a presenter suggests that it might be a part of a video explaining the process.

4.  **Specific technical details:**
    *   The screenshot indicates that the user is setting up a GitHub Pages website.
    *   The "Source" option set to "None" likely refers to the repository source for the website.
    *   The "Theme Chooser" suggests customization options for the website's appearance.

*Original image: ![Host a website using GitHub Pages](https://i.ytimg.com/vi_webp/WqOXxoGSpbs/sddefault.webp)*](https://youtube.com/shorts/WqOXxoGSpbs)

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a screenshot of a GitHub Codespaces environment. It shows the user interface of a code editor with multiple panels and tabs. The primary areas of focus are the GitHub Actions workflow and the corresponding logs or output.

2.  **Key Elements, Text, and Data:**

    *   **Navigation/File Structure (Left Panel):**
        *   "GITHUB ACTIONS" with a "CURRENT BRANCH" selected.
        *   A collapsible list of "WORKFLOWS" with an expanded "InvitationLabel".
        *   Specific workflow steps listed such as "#4404", "#4403", "#4402", "#4401", "#4400" with "Add collaborator", "Set up job", "Perform invitation action", "Complete job".
        *   There's also other workflow entries, such as #4399 through #4391.
    *   **Code Editor/Output Panel (Right Panel):**
        *   "Extension: GitHub Actions" is the active tab.
        *   Detailed logs from a GitHub Actions run related to "Add collaborator".
        *   Timestamped log entries showing the progression of the workflow.
        *   Security related logs as "SecurityEvents: write".
        *   Information like the secret source being Actions, preparation of the workflow directory and required actions.
        *   Repository details like 'blackgirlbytes/invite-collaborator-action@main' being downloaded.
        *   The environment variables like CLIENT\_ID, APP\_ID, CLIENT\_SECRET, WEBHOOK\_SECRET, PRIVATE\_KEY, INSTALLATION\_ID.
        *   Information about the event values like Repo Owners community, and the commenter's username being Mridul5.
    *   **Top Bar:**
        *   Various tabs indicating open files or services like "Codespace templates", "Index.js - codespaces-neo", "Github Marketplace - Action"
        *   "maintainer-requests [Codespaces]" indicating the project or repository context.
        *   "Quokka: What's New" and "#4799892989 - Add collaborator! X"
    *   **Bottom Bar:**
        *   Indicates it's running in a "Codespaces" environment.
        *   Branch details ("main").
        *   Encoding/layout details ("Spaces: 4 Plain Text Layout: U.S.").

3.  **Purpose or Educational Value:**

    *   Demonstrates the GitHub Actions workflow setup and execution.
    *   Illustrates how to use GitHub Actions for automating tasks within a repository.
    *   Shows how to handle sensitive information (secrets) within GitHub Actions.
    *   Provides insights into debugging or monitoring the execution of a GitHub Actions workflow, especially when dealing with API integrations or automated processes.
    *   Shows the different actions for adding collaborators to a github repo, performing invites, and setting up related tasks.

4.  **Specific Technical Details:**

    *   GitHub Actions is being used to automate the process of adding collaborators to a repository.
    *   The workflow uses secrets to authenticate with external services or APIs.
    *   The logs provide detailed information about the steps being executed, including timestamps and any errors or warnings.
    *   The repository being referenced is 'blackgirlbytes/invite-collaborator-action@main'.
    *   The user involved is "Mridul5".

In summary, the image captures a developer's view of a GitHub Codespaces environment, showcasing the execution of a GitHub Actions workflow designed to automate collaborator invitation, alongside the configurations and logs associated with this process. It is relevant for educational purposes in demonstrating workflow automation, secret management, and debugging in the context of GitHub repositories.

*Original image: ![Deploy your first GitHub Pages Website](https://i.ytimg.com/vi_webp/sT_zXIX3ZA0/sddefault.webp)*](https://youtu.be/sT_zXIX3ZA0)
