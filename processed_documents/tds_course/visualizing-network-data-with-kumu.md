---
source_url: "https://tds.s-anand.net/#/visualizing-network-data-with-kumu"
---

## Visualizing Network Data with Kumu

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a screenshot of a computer screen showing several browser tabs. One of the prominent tabs is a Wikipedia page titled "Sparse matrix." Additionally, a person's face is visible in the lower right corner.

2.  **Key Elements, Text, and Data:**

    *   **Sparse Matrix Wikipedia Page:** The Wikipedia page displays information related to sparse matrices, including a definition, examples, and representation methods. Text visible on the page includes:

        *   "Sparse matrix"
        *   "total number of nonzeros above row j. The last element is NNZ, i.e., the fictitious index in V immediately after the last valid index NNZ - 1"
        *   An example matrix:
            ```
            (5 0 0 0)
            (0 8 0 0)
            (0 0 3 0)
            (0 6 0 0)
            ```
        *   "is a 4x4 matrix with 4 nonzero elements, hence"
        *   Arrays V, COL\_INDEX, and ROW\_INDEX:
            ```
            V          = [5 8 3 6]
            COL_INDEX  = [0 1 2 1]
            ROW_INDEX  = [0 1 2 3 4]
            ```
        *   "assuming a zero-indexed language. To extract a row, we first define:"
            ```
            row_start = ROW_INDEX[row]
            row_end   = ROW_INDEX[row + 1]
            ```
        *   "Then we take slices from V and COL\_INDEX starting at row\_start and ending at row\_end."
        *   "To extract the row 1 (the second row) of this matrix we set row\_start=1 and row\_end=2. Then we make the slices V[1:2] = [8] and COL\_INDEX[1:2] = [1]. We now know that in row 1 we have one element at column 1 with value 8."
        *   "In this case the CSR representation contains 13 entries, compared to 16 in the original matrix. The CSR format saves on memory only when NNZ < (m * n)"
        *   An example matrix:
            ```
            (10 20  0  0  0)
            ( 0 30  0 40  0)
            ( 0  0 50 60 70)
            ( 0  0  0  0 80)
            ```

    *   **Browser Tabs:** Other visible browser tabs have the following titles:
        *   "DataPrepForKumu.ipynb - Colab"
        *   "Kumu"
        *   "Actor pairs · Actor network · K"
        *   "MatrixMul - Network Example"

    *   **Person:** In the lower right corner, a person with a beard is visible. They are wearing a blue shirt.

3.  **Purpose or Educational Value:** The image appears to be related to a tutorial or educational resource on sparse matrices and their applications. The Wikipedia page provides a foundational understanding of sparse matrices and how they are represented in computer science. The other tabs suggest an application of sparse matrices within a network analysis context, possibly using a tool like Kumu or a similar network visualization platform. The inclusion of the person suggests a video or presentation accompanying the material.

4.  **Specific Technical Details:**

    *   The sparse matrix example illustrates the concept of representing a matrix with mostly zero elements in a more memory-efficient way.
    *   The arrays V, COL\_INDEX, and ROW\_INDEX are part of the Compressed Sparse Row (CSR) or similar sparse matrix representation.
    *   The Python-like code snippets demonstrate how to extract rows from the sparse matrix representation.
    *   The reference to "NNZ" (number of non-zero elements) is crucial for understanding the efficiency gains of using sparse matrix representations.
    *   The condition "NNZ < (m * n)" highlights when using a sparse format becomes beneficial (when the number of non-zero elements is significantly smaller than the total number of elements in the matrix).

*Original image: ![Visualizing network data with Kumu](https://i.ytimg.com/vi_webp/OndB17bigkc/sddefault.webp)*](https://youtu.be/OndB17bigkc)

- [Kumu](https://kumu.io)
- [IMDB data](https://developer.imdb.com/non-commercial-datasets/)
- [Jupyter Notebook](https://colab.research.google.com/drive/1CHR68fw7lZC9H2JtVW4LXpUvNwfM_VE-?usp=sharing)

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image displays a Google Colaboratory (Colab) notebook interface along with a portion of a Google Meet video call. The Colab notebook seems to be used for data analysis or preparation, while the Meet call shows a participant.

2.  **Key Elements, Text, or Data Visible:**
    *   **Colab Notebook Interface:** The Colab notebook shows Python code for data manipulation. There is a data table with columns like "tconst", "titleType", "primaryTitle", and "startYear" which suggests the notebook is being used for data preparation.
        *   Example values in the table include "tt0001848" for "tconst", "episode" for "titleType", "Episode #3.17" for "primaryTitle", and "2013" for "startYear".
    *   **Data Types:** Underneath the table, there is information about the data types of each column: "titleType" (object), "primaryTitle" (object), "startYear" (object).
    *   **Code Snippet:** There is a code snippet: `[tiitle)['startYear'] > '2010'`. This seems to be a filter operation on the dataset where the `startYear` is checked if it is greater than `2010`.
    *   **Result of the code:** Under the code snippet, there are boolean results (False) suggesting the filtering is taking place, but no entries satisfy the condition of `startYear` being more recent than 2010.
    *   **Google Meet Call:** A portion of a Google Meet call is visible on the right side of the image, displaying a person named "Rohith Srinivaas".

3.  **Purpose or Educational Value:** The image demonstrates how a Colab notebook is used for data analysis or preparation tasks. Specifically, it shows:
    *   Importing or accessing data (represented by the visible table).
    *   Viewing data types.
    *   Filtering data based on conditions.
    *   It also gives insight into how programmers are using video calls to share their work and to discuss projects with others.

4.  **Specific Technical Details:**
    *   The data analysis is likely being done with Python and popular libraries such as Pandas (but not visible).
    *   Colab is a cloud-based Python environment, enabling users to run code without needing to set up a local environment.
    *   The line of code `[tiitle)['startYear'] > '2010'` refers to a conditional comparison, using pandas as a library.

*Original image: ![Network analysis – filtering by year](https://i.ytimg.com/vi_webp/oi4fDzqsCes/sddefault.webp)*](https://youtu.be/oi4fDzqsCes)
