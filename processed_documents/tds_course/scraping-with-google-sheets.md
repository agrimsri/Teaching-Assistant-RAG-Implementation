---
source_url: "https://tds.s-anand.net/#/scraping-with-google-sheets"
---

## Scraping with Google Sheets

[**[Image Description]**: Here is a detailed description of the image:

1.  **Image Content:** The image is a screenshot of a Google Docs/Sheets document displayed in a web browser. The document presents information about using the `IMPORTHTML` function in Google Sheets for web scraping. A person is seen in the bottom right corner of the image.

2.  **Key Elements, Text, and Data:**
    *   **Title:** The document's title is likely related to the `IMPORTHTML` function. There are multiple tabs open at the top, indicating different Google Sheet documents or web pages related to the function and demographics of India.
    *   **Sample Usage:**
        *   `IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India", "table", 4)`: This is an example of how to use the `IMPORTHTML` function to extract data from a web page. It specifies the URL, the query type as "table", and the index of the table to retrieve (table #4).
        *   `IMPORTHTML(A2, B2, C2)`: This indicates that the URL, query, and index can be specified as cell references in the spreadsheet.
    *   **Syntax:**
        *   `IMPORTHTML(url, query, index)`: This outlines the general syntax of the function.
    *   **Parameters Breakdown:**
        *   `url`:  The description states that this is the URL of the page to examine, including the protocol (e.g., `http://`). It also notes that the URL should be in quotation marks or a cell reference.
        *   `query`:  Explains that this parameter is either "list" or "table" depending on the type of data structure on the web page.
        *   `index`:  This is the index number of the table or list, starting at 1, that you want to extract.

3.  **Purpose and Educational Value:** The image serves as a guide or tutorial on how to use the `IMPORTHTML` function in Google Sheets. It explains the syntax, provides an example, and clarifies the meaning of each parameter. The information is useful for users who want to extract data from websites directly into their spreadsheets without needing to write custom code.

4.  **Technical Details:**
    *   `IMPORTHTML` function: This is a built-in function in Google Sheets that allows users to import data from tables or lists on a webpage.
    *   Web Scraping: The process of extracting data from websites, often automated, which this function facilitates.
    *   Parameters: Understanding the purpose and format of the `url`, `query`, and `index` parameters is crucial for using the function correctly.
    *   Quotation marks: The reminder that the URL parameter must be enclosed in quotation marks, or else must reference a valid cell.

*Original image: ![Scraping with Google Sheets](https://i.ytimg.com/vi_webp/eYQEk7XJM7s/sddefault.webp)*](https://youtu.be/eYQEk7XJM7s)

You'll learn how to [import tables on the web using Google Sheets's `=IMPORTHTML()` formula](https://support.google.com/docs/answer/3093339?hl=en), covering:

- **Import HTML Formula**: Use =IMPORTHTML(URL, "query", index) to fetch tables or lists from a web page.
- **Granting Access**: Allow access for formulas to fetch data from external sources.
- **Checking Imported Data**: Verify if the imported table matches the data on the web page.
- **Handling Errors**: Understand common issues and how to resolve them.
- **Sorting Data**: Copy imported data as values and sort it within Google Sheets.
- **Freezing Rows**: Use frozen rows to maintain headers while sorting.
- **Live Formulas**: Learn how web data updates automatically when the source changes.
- **Other Import Functions**: IMPORTXML, IMPORTFEED, IMPORTRANGE, and IMPORTDATA for advanced data fetching options.

Here are links used in the video:

- [Google sheet used in the video](https://docs.google.com/spreadsheets/d/1Qp_YTh1-hJHxjMWE_GofkvLIKgEdKxb6NFImpId3z9o/view)
- [`IMPORTHTML()`](https://support.google.com/docs/answer/3093339)
- [`IMPORTXML()`](https://support.google.com/docs/answer/3093342)
- [Demographics of India](https://en.wikipedia.org/wiki/Demographics_of_India)
- [List of highest grossing Indian films](https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films)
