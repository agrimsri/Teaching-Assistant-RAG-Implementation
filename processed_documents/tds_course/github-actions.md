---
source_url: "https://tds.s-anand.net/#/github-actions"
---

## CI/CD: GitHub Actions

[GitHub Actions](https://github.com/features/actions) is a powerful automation platform built into GitHub. It helps automate your development workflow - running tests, deploying applications, updating datasets, retraining models, etc.

- Understand the basics of [YAML configuration files](https://docs.github.com/en/actions/writing-workflows/quickstart)
- Explore the [pre-built actions from the marketplace](https://github.com/marketplace?type=actions)
- How to [handle secrets securely](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Triggering a workflow](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
- Staying within the [free tier limits](https://docs.github.com/en/billing/managing-billing-for-your-products/managing-billing-for-github-actions/about-billing-for-github-actions)
- [Caching dependencies to speed up workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows)

Here is a sample `.github/workflows/iss-location.yml` that runs daily, appends the International Space Station location data into `iss-location.json`, and commits it to the repository.

```yaml
name: Log ISS Location Data Daily

on:
  schedule:
    # Runs at 12:00 UTC (noon) every day
    - cron: "0 12 * * *"
  workflow_dispatch: # Allows manual triggering

jobs:
  collect-iss-data:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Fetch ISS location data
        run: | # python
          uv run --with requests python << 'EOF'
          import requests

          data = requests.get('http://api.open-notify.org/iss-now.json').text
          with open('iss-location.jsonl', 'a') as f:
              f.write(data + '\n')
          'EOF'

      - name: Commit and push changes
        run: | # shell
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add iss-location.jsonl
          git commit -m "Update ISS position data [skip ci]" || exit 0
          git push
```

Tools:

- [GitHub CLI](https://cli.github.com/): Manage workflows from terminal
- [Super-Linter](https://github.com/github/super-linter): Validate code style
- [Release Drafter](https://github.com/release-drafter/release-drafter): Automate releases
- [act](https://github.com/nektos/act): Run actions locally

[**[Image Description]**: Here is a detailed description of the image:

1.  **Image Description:**
    *   The image is a thumbnail for a video or presentation, likely related to software development and specifically focusing on Github Actions.
    *   The background is split diagonally: the left side is a dark gray, and the right side is a vibrant blue.
    *   There is a cartoon mascot character on the left side, text prominently displayed on the dark gray side, and an abstract icon on the blue side.

2.  **Key Elements, Text, and Data:**
    *   **Text:** The primary text reads "Github Actions" in a large, white, sans-serif font. The word "Github" is above the cartoon mascot and the word "Actions" is below.
    *   **Cartoon Mascot:** The mascot appears to be a combination of the Github Octocat and a humanoid character. It has an Octocat head, large eyes, and is wearing a futuristic outfit with jetpack-like elements.
    *   **Abstract Icon:** The icon on the right consists of several circles connected by lines. The top circle contains a play symbol (triangle pointing right), and the two circles below it contain ellipses. The connecting lines suggest a flow or process.

3.  **Purpose and Educational Value:**
    *   The image serves as an introduction to the topic of Github Actions. The title text and accompanying visual elements aim to draw the viewer's attention and convey the subject matter.
    *   The title text along with the alt text suggests it will educate viewers on the fundamentals of GitHub Actions for CI/CD (Continuous Integration and Continuous Deployment).

4.  **Specific Technical Details:**
    *   The icon on the right side visually hints at the concept of CI/CD pipelines, indicating a series of steps or tasks connected in a workflow.
    *   The title directly mentions Github Actions, which is a popular platform for automating software workflows, including building, testing, and deploying code.

In summary, the image is a visually appealing thumbnail designed to introduce the topic of Github Actions for CI/CD. It uses a combination of text, a mascot character, and an abstract icon to attract attention and provide a basic understanding of the subject matter.

*Original image: ![Github Actions CI/CD - Everything you need to know to get started](https://i.ytimg.com/vi_webp/mFFXuXjVgkU/sddefault.webp)*](https://youtu.be/mFFXuXjVgkU)

- [How to handle secrets in GitHub Actions](https://youtu.be/1tD7km5jK70)
