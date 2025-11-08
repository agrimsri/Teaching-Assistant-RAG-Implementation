---
source_url: "https://tds.s-anand.net/#/scraping-imdb-with-javascript"
---

## Scraping IMDb with JavaScript

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image shows a screenshot of a web browser displaying a ChatGPT conversation on the topic of scraping the IMDb website using browser JavaScript. The conversation is about troubleshooting a JavaScript code snippet involving `querySelectorAll` and extracting text content. There is also a video feed of a man in the bottom right corner of the screenshot.

2.  **Key elements, text, or data visible:**
    *   **Code Snippet:** The code snippet in question is: `item.querySelectorAll(".cli-title-metadata-item:nth-child(1)").text`. This is likely part of a larger script to extract data from IMDb.
    *   **Error Explanation:** ChatGPT is providing a list of possible reasons why the code is not working as expected. These reasons include:
        *   **No Matching Elements:** The query selector might not find any matching elements.
        *   **Wrong Pseudo-Class:** The `:nth-child(1)` pseudo-class might be inappropriate.
        *   **Typo in Class Name:** There might be a typo in the class name `.cli-title-metadata-item`.
        *   **Incorrect Usage of `querySelectorAll`:** `querySelectorAll` returns a `NodeList`, so you need to access the element using `[0]` before getting the `text`.
        *   **Missing Text Property:** The property should be `.textContent` or `.innerText`.
    *   **UI Elements:** The browser's address bar shows a URL for `chatgpt.com`. The screenshot also shows the taskbar on Windows, with icons for several applications.
    *   **Video Feed:** There is a small video feed of a man in the bottom-right corner.

3.  **Purpose or educational value:** The image has educational value by demonstrating common issues encountered when scraping websites using JavaScript, particularly when dealing with selectors, DOM structure, and extracting text content from elements. It highlights the importance of:
    *   Correctly identifying and using CSS selectors to target elements.
    *   Understanding the difference between `querySelector` and `querySelectorAll` and how to access elements in a `NodeList`.
    *   Knowing the correct properties (e.g., `textContent`, `innerText`) to extract text from DOM elements.
    *   Checking for typos and ensuring the correctness of class names.
    *   Being aware that elements might be loaded dynamically, affecting the availability of elements when the script runs.

4.  **Specific technical details:**
    *   The code targets elements with the class `.cli-title-metadata-item` that are the first child of their parent within the `item` element.
    *   The use of `querySelectorAll` suggests the possibility of multiple elements matching the selector.
    *   The code attempts to access the `text` property directly on the `NodeList`, which is incorrect. The correct way to access text content would involve selecting the element using an index (e.g., `[0]`) and then using either `textContent` or `innerText`.
    *   The image suggests troubleshooting a JavaScript script that automates scraping of website data.

*Original image: ![Scraping the IMDb with Browser JavaScript](https://i.ytimg.com/vi_webp/YVIKZqZIcCo/sddefault.webp)*](https://youtu.be/YVIKZqZIcCo)

You'll learn how to scrape the [IMDb Top 250 movies](https://www.imdb.com/chart/top) directly in the browser using JavaScript on the Chrome DevTools, covering:

- **Access Developer Tools**: Use F12 or right-click > Inspect to open developer tools in Chrome or Edge.
- **Inspect Elements**: Identify and inspect HTML elements using the Elements tab.
- **Query Selectors**: Use `document.querySelectorAll` and `document.querySelector` to find elements by CSS class.
- **Extract Text Content**: Retrieve text content from elements using JavaScript.
- **Functional Programming**: Apply [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
  and [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
  for concise data processing.
- **Data Structuring**: Collect and format data into an array of arrays.
- **Copying Data**: Use the copy function to transfer data to the clipboard.
- **Convert to Spreadsheet**: Use online tools to convert JSON data to CSV or Excel format.
- **Text Manipulation**: Perform text splitting and cleaning in Excel for final data formatting.

Here are links and references:

- [IMDB Top 250 movies](https://www.imdb.com/chart/top/)
- [Learn about Chrome Devtools](https://developer.chrome.com/docs/devtools/overview/)
