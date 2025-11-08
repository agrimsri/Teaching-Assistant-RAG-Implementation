---
source_url: "https://tds.s-anand.net/#/npx"
---

## JavaScript tools: npx

[npx](https://docs.npmjs.com/cli/v8/commands/npx) is a command-line tool that comes with npm (Node Package Manager) and allows you to execute npm package binaries and run one-off commands without installing them globally. It's essential for modern JavaScript development and data science workflows.

For data scientists, npx is useful when:

- Running JavaScript-based data visualization tools
- Converting notebooks and documents
- Testing and formatting code
- Running development servers

Here are common npx commands:

```bash
# Run a package without installing
npx http-server .                # Start a local web server
npx prettier --write .           # Format code or docs
npx eslint .                     # Lint JavaScript
npx typescript-node script.ts    # Run TypeScript directly
npx esbuild app.js               # Bundle JavaScript
npx jsdoc .                      # Generate JavaScript docs

# Run specific versions
npx prettier@3.2 --write .        # Use prettier 3.2

# Execute remote scripts (use with caution!)
npx github:user/repo            # Run from GitHub
```

Watch this introduction to npx (6 min):

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image is a title card, likely from a video or presentation. It features text and a logo set against a dark gray background with a horizontal red bar at the bottom.

2.  **Key elements, text, or data visible:**
    *   **Text:** The text "what you can do with" is prominently displayed in a clean, sans-serif, white font on the left side of the image.
    *   **Logo:** The logo consists of the letters "np" enclosed in a red rectangle, followed by a stylized white "X" with a red outline. The X is positioned to the right of the "np" box.
    *   **Horizontal Bar:** A red horizontal bar runs across the bottom of the image.
    *   **Alt text:** "What you can do with npx (6 min)"

3.  **The purpose or educational value:** The image serves as a title card that sets the stage for content about "npx". Based on the text and the implied time length, it's likely a video or presentation explaining the capabilities and uses of npx. The purpose is to inform viewers about what they can accomplish with npx.

4.  **Any specific technical details:**
    *   "npx" likely refers to the Node Package Executor, a tool that comes with npm (Node Package Manager) version 5.2.0 and later. It allows you to run packages without installing them globally.

In summary, the image is a title card that introduces a video or presentation about the Node Package Executor (npx), indicating that the content will cover its capabilities and usage.

*Original image: ![What you can do with npx (6 min)](https://i.ytimg.com/vi_webp/55WaAoZV_tQ/sddefault.webp)*](https://youtu.be/55WaAoZV_tQ)
