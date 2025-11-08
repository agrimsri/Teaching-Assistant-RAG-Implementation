---
source_url: "https://tds.s-anand.net/#/marimo"
---

## Interactive Notebooks: Marimo

[Marimo](https://marimo.app/) is a new take on notebooks that solves some headaches of Jupyter. It runs cells reactively - when you change one cell, all dependent cells update automatically, just like a spreadsheet.

Marimo's cells can't be run out of order. This makes Marimo more reproducible and easier to debug, but requires a mental shift from the Jupyter/Colab way of working.

It also runs Python directly in the browser and is quite interactive. [Browse the gallery of examples](https://marimo.io/gallery). With a wide variety of interactive widgets, It's growing popular as an alternative to Streamlit for building data science web apps.

Common Operations:

```python
# Create new notebook
uvx marimo new

# Run notebook server
uvx marimo edit notebook.py

# Export to HTML
uvx marimo export notebook.py
```

Best Practices:

1. **Cell Dependencies**
   - Keep cells focused and atomic
   - Use clear variable names
   - Document data flow between cells
2. **Interactive Elements**

   ```python
   # Add interactive widgets
   slider = mo.ui.slider(1, 100)
   # Create dynamic Markdown
   mo.md(f"{slider} {"🟢" * slider.value}")
   ```

3. **Version Control**
   - Keep notebooks are Python files
   - Use Git to track changes
   - Publish on [marimo.app](https://marimo.app/) for collaboration

[**[Image Description]**: Here is a detailed description of the image:

1.  **Image Content:** The image is a screenshot featuring a software interface, likely a data analysis or machine learning notebook environment. The top portion displays a row of images depicting the digit "2" in various handwritten styles. Below this is a data table accompanied by bar charts, and in the bottom-right corner there is a presentation screen with a man presenting to an audience. The bottom displays status messages related to code execution.

2.  **Key Elements, Text, and Data:**

    *   **Digit Images:** A series of handwritten digits, all representing the number "2". These are likely part of a dataset used for training or testing a digit recognition model.
    *   **Data Table:** A table showing data associated with the digit images. The columns include:
        *   "index": Numerical identifiers (e.g., 62168, 15610, 61226).
        *   "x": Numerical values (e.g., -0.43127555, -0.942177, -0.4252105).
        *   "y": Numerical values (e.g., -1.3145471, -1.1613866, -1.3749739).
        *   "digit": Categorical values, likely representing the actual digit each image represents (e.g., 8, 7, 6, 3).
    *   **Bar Charts:** Graphical representations of the data from the table. There are separate bar charts for "index", "x", "y", and "digit" with labels and value ranges along the x-axis.
    *   **Checkboxes:** There are checkboxes next to each entry in the data table, possibly for selecting specific data rows. The first checkbox is checked.
    *   **Top Panel:** At the top, there's a title "Here's a preview of the images you've selected" and tool icons for interface customization and controls.
    *   **Lower Panel:** At the bottom, there is text indicating "on startup: autorun" and "on cell change: autorun", suggesting the environment has a reactive or automatically updating nature.
    *   **Bottom Right Panel:** A man at the front of an audience presenting a cloud logo and logos for Meta, Bloomberg, Python, and Netflix.

3.  **Purpose and Educational Value:** The image appears to illustrate a data exploration or data analysis step within a machine learning workflow. It demonstrates how data points (images of digits) are associated with numerical features ("x", "y") and their corresponding labels ("digit"). It could be used for:

    *   Teaching data visualization techniques.
    *   Explaining the structure of datasets used in machine learning.
    *   Demonstrating the interaction between raw data, feature representation, and labels.
    *   Highlighting the use of a reactive notebook environment for data analysis.

4.  **Specific Technical Details:**

    *   The user interface is likely that of a Python notebook environment, possibly a custom one.
    *   The status messages "on startup: autorun" and "on cell change: autorun" indicate that the notebook is reactive, i.e., it automatically updates computations whenever the code or data changes.
    *   The presence of machine learning-related elements (digits, features, labels) suggests that this image is related to a machine learning task, specifically digit recognition or classification.
    *   "marimo: an open-source reactive notebook for Python" is used as alt text in the prompt to provide the context for this screenshot which is the name of the application and a basic descriptor.

*Original image: !["marimo: an open-source reactive notebook for Python" - Akshay Agrawal (Nbpy2024)](https://i.ytimg.com/vi_webp/9R2cQygaoxQ/sddefault.webp)*](https://youtu.be/9R2cQygaoxQ)
