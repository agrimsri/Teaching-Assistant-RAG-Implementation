---
source_url: "https://tds.s-anand.net/#/git"
---

## Version Control: Git, GitHub

[Git](https://git-scm.com/) is the de facto standard for version control of software (and sometimes, data as well). It's a system that keeps track of changes you make to files and folders. It allows you to revert to a previous state, compare changes, etc. It's a central tool in any developer's workflow.

[GitHub](https://github.com/) is the most popular hosting service for Git repositories. It's a website that shows your code, allows you to collaborate with others, and provides many useful tools for developers.

Watch these introductory videos to learn the basics of Git and GitHub (98 min):

[**[Image Description]**: Here's a detailed description of the image:

1.  **What the image shows:** The image is a title card or cover image for a Git tutorial. It features a stylized logo and text on a textured background.

2.  **Key elements, text, or data visible:**
    *   The Git logo: A stylized, reddish-orange diamond shape with branching lines and circular nodes, resembling a simplified representation of version control branching.
    *   The word "git" in a bold, dark font is placed to the right of the Git logo.
    *   A horizontal white line separates the logo and "git" from the lower portion of the image.
    *   The text "Command-Line" and "Fundamentals" is stacked below the white line. The text is large, bold, and in a dark color.

3.  **The purpose or educational value:** The image serves as a title card to introduce a tutorial about Git command-line fundamentals, targeted at beginners. The text suggests the tutorial will cover basic concepts and commands related to Git version control.

4.  **Any specific technical details:** The background has a slightly distressed or textured appearance. This is likely a design choice to give the image a more visually appealing or less sterile look. The emphasis on "Command-Line" suggests the tutorial will focus on using Git through the command line interface (CLI) rather than a graphical user interface (GUI).

*Original image: ![Git Tutorial for Beginners: Command-Line Fundamentals (30 min)](https://i.ytimg.com/vi_webp/HVsySz-h9r4/sddefault.webp)*](https://youtu.be/HVsySz-h9r4)

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a thumbnail from a YouTube video, likely serving as an introduction to a course or tutorial. It features a dark blue background with white graphical elements and text.

2.  **Key Elements & Text:**
    *   **Logos:** There are three logos across the top. The first one on the left shows a branch-like structure. The second one shows a flame and the third logo shows a silhouetted cat with a curling tail inside a circle.
    *   **Text:** The main text on the image reads "Git and GitHub Crash Course" in large, bold, white letters.

3.  **Purpose & Educational Value:**
    *   The image is designed to attract viewers interested in learning about Git and GitHub. The phrase "Crash Course" implies a fast-paced, comprehensive introduction to these tools.
    *   The logos signify that the course focuses on Git (version control), GitHub (a web-based hosting service for Git repositories), and potentially Firebase(the logo with the flame). The image hints at providing foundational knowledge that can benefit software developers, web developers, or anyone working on collaborative projects.

4.  **Technical Details:**
    *   Git is a distributed version control system for tracking changes in source code during software development.
    *   GitHub is a web-based platform that provides hosting for software development version control using Git.
    *   The logos are widely recognized within the software development and technology communities as visual representations of Git and GitHub.

*Original image: ![Git and GitHub for Beginners - Crash Course (68 min)](https://i.ytimg.com/vi_webp/RGOj5yH7evk/sddefault.webp)*](https://youtu.be/RGOj5yH7evk)

Essential Git Commands:

```bash
# Repository Setup
git init                   # Create new repo
git clone url              # Clone existing repo
git remote add origin url  # Connect to remote

# Basic Workflow
git status                 # Check status
git add .                  # Stage all changes
git commit -m "message"    # Commit changes
git push origin main       # Push to remote

# Branching
git branch                 # List branches
git checkout -b feature    # Create/switch branch
git merge feature          # Merge branch
git rebase main            # Rebase on main

# History
git log --oneline          # View history
git diff commit1 commit2   # Compare commits
git blame file             # Show who changed what
```

Best Practices:

1. **Commit Messages**

   ```bash
   # Good commit message format
   type(scope): summary

   Detailed description of changes.

   # Examples
   feat(api): add user authentication
   fix(db): handle null values in query
   ```

2. **Branching Strategy**

   - main: Production code
   - develop: Integration branch
   - feature/\*: New features
   - hotfix/\*: Emergency fixes

3. **Code Review**
   - Keep PRs small (<400 lines)
   - Use draft PRs for WIP
   - Review your own code first
   - Respond to all comments

Essential Tools

- [GitHub Desktop](https://desktop.github.com/): GUI client
- [GitLens](https://gitlens.amod.io/): VS Code extension
- [gh](https://cli.github.com/): GitHub CLI
- [pre-commit](https://pre-commit.com/): Git hooks
