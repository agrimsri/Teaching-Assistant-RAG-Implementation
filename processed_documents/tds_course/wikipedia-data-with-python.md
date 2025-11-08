---
source_url: "https://tds.s-anand.net/#/wikipedia-data-with-python"
---

## Wikipedia Data with Python

[**[Image Description]**: Here's a detailed description of the image:

1. **What the image shows:** The image is a presentation slide, likely part of a lecture or online course. It appears to be from a series on "Tools in Data Science" from IIT Madras Online Degree program.

2. **Key elements, text, or data visible:**
   - The main title is "Get the data: Wikimedia". This indicates the topic of the slide is related to obtaining data from the Wikimedia project, which encompasses Wikipedia and other related sites.
   - The course name is explicitly stated as "TOOLS IN DATA SCIENCE."
   - The instructor's name is "ANAND S".
   - The tutorial instructor's name is "DIBU PHILIP."
   - The IIT Madras Online Degree logo is in the upper right corner.

3. **The purpose or educational value:** The slide serves as an introduction to a section or module on data acquisition techniques using Wikimedia data. It likely aims to introduce learners to the process of extracting and utilizing data from Wikimedia projects for data science applications.

4. **Any specific technical details:** The implied technical detail is the use of Wikimedia data for data science, which suggests the potential use of programming libraries or APIs to access and process this data.

*Original image: ![Wikipedia data with Wikimedia Python library](https://i.ytimg.com/vi_webp/b6puvm-QEY0/sddefault.webp)*](https://youtu.be/b6puvm-QEY0)

You'll learn how to scrape data from Wikipedia using the `wikipedia` Python library, covering:

- **Installing and Importing**: Use pip install to get the Wikipedia library and import it with import wikipedia as wk.
- **Keyword Search**: Use the search function to find Wikipedia pages containing a specific keyword, limiting results with the results argument.
- **Fetching Summaries**: Use the summary function to get a concise summary of a Wikipedia page, limiting sentences with the sentences argument.
- **Retrieving Full Pages**: Use the page function to obtain the full content of a Wikipedia page, including sections and references.
- **Accessing URLs**: Retrieve the URL of a Wikipedia page using the url attribute of the page object.
- **Extracting References**: Use the references attribute to get all reference links from a Wikipedia page.
- **Fetching Images**: Access all images on a Wikipedia page via the images attribute, which returns a list of image URLs.
- **Extracting Tables**: Use the pandas.read_html function to extract tables from the HTML content of a Wikipedia page, being mindful of table indices.

Here are links and references:

- [Wikipedia Library - Notebook](https://colab.research.google.com/drive/1-w8Jo6xcQs2jK0NxNddPW4HVCZhXmTBe)
- Learn about the [`wikipedia` package](https://wikipedia.readthedocs.io/en/latest/)

**NOTE**: Wikipedia is constantly edited. The page may be different now from when the video was recorded. Handle accordingly.
