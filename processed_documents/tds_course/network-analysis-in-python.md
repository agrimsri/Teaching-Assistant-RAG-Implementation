---
source_url: "https://tds.s-anand.net/#/network-analysis-in-python"
---

## Network Analysis in Python

[**[Image Description]**: Here's a detailed description of the image:

**1. What the image shows:**

The image is a screenshot of a Google Colaboratory (Colab) notebook focused on analyzing a movie actor network. It shows code cells, text cells, and a data frame being displayed within the Colab environment. There is also a person in the lower-right corner.

**2. Key elements, text, or data visible:**

*   **Colab Notebook:** The screenshot is from Google Colab, indicated by the Colab logo, file menu (File, Edit, View, Insert, Runtime, Tools, Help), and the "IMDB Network\_dj - Colaboratory" title.
*   **Data Frame:** A data frame containing information about actors is visible. The columns are:
    *   An index column with numerical values like 1308, 63, 5305, etc.
    *   An "nm" column containing unique identifiers, presumably from IMDb (e.g., "nm0001744," "nm0000078").
    *   The name of the actor (e.g., "Tom Sizemore," "John Wayne," "Fermando Fernán Gómez," "Andy Lau").
    *   A year value, likely the birth year or a significant year related to their career (e.g., 1961.0, 1907.0, 1921.0).
    *   "0" columns (likely representing other metrics about the actor)
    *   A numerical value (e.g., 139, 135, 131, 128)
*   **Code Cell:** A code cell is at the bottom of the visible area of the notebook. The code snippet shows:
    `klusters_in[clusters_in['cluster"]=-1].sort_values('freq', ascending-False).head(20)`
    This code likely filters a DataFrame called `klusters_in`, selects a subset where the 'cluster' column equals -1, sorts the results by the 'freq' column in descending order, and then displays the top 20 rows using `.head(20)`.
*   **Text in notebook:** "IMDB Network\_dj" is shown in the notebook.
*   **Status Indicator:** A status message at the bottom indicates "0s completed at 11:43 PM," suggesting a code execution status and timestamp.
*   **Person:** The lower-right shows a person (likely the presenter or instructor) whose face is visible.
*   **Browser elements:** The top of the screenshot shows the browser interface with standard controls (back, forward, refresh), the URL, and browser tabs with titles like "IMDB Network\_dj - Colaboratory" and "MatrixMul - Network Example."

**3. The purpose or educational value:**

The image suggests an educational context, likely a tutorial or demonstration of network analysis using Python and the IMDb dataset. The Colab notebook is used for:

*   **Data manipulation:** Filtering, sorting, and displaying data related to actors.
*   **Network analysis:** The name "IMDB Network\_dj" implies an analysis of actor connections and collaborations within movies.
*   **Code demonstration:** The code snippet provides an example of how to perform specific data operations in Python (likely using Pandas).
*   **Instructional Material:** The instructor in the corner suggests that this is recorded or live tutorial/instruction.

**4. Specific technical details:**

*   **Programming Language:** Python (likely due to the code syntax).
*   **Libraries:** The code likely uses the Pandas library for data frame manipulation. The mention of "cluster" implies a clustering algorithm has been applied to the actor network, perhaps using a library like scikit-learn.
*   **Data Source:** The data comes from or is related to the IMDb database, a large source of movie and actor information.
*   **Algorithm:** Clustering algorithms is likely used to define and group actors/nodes with higher frequency/similar features.
*   **Tool:** Google Colaboratory.

In summary, the image showcases a Python-based data analysis project, most likely as part of a learning experience, to analyze and visualize actor relationships using data from IMDb.

*Original image: ![Talk: Exploring the Movie Actor Network in Python](https://i.ytimg.com/vi_webp/uPL3VuRqOy4/sddefault.webp)*](https://youtu.be/uPL3VuRqOy4)

You'll learn how to use network analysis to identify clusters and connections between nodes in a dataset, covering:

- **Network Construction**: Build a network from the IMDB database, where nodes represent actors and edges represent shared movie appearances.
- **Clustering**: Apply clustering techniques to detect communities within the network, using scikit-learn's network library.
- **Matrix Operations**: Utilize matrix operations to efficiently analyze actor relationships and interactions.
- **Community Detection**: Implement algorithms to identify and interpret clusters, examining how different actor clusters are connected.
- **Application of Findings**: Explore practical applications of network analysis, such as social network analysis and its potential uses in various domains.

Here are links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1VRlAOfREGwflv7v2VmN-6O_wqRno4Xcq?usp=sharing)
- [Exploring the Movie Actor Network in Python](https://youtu.be/6hzLw80qxto)
- [Jupyter Notebook - Shortest Path](https://colab.research.google.com/drive/1-b0pA1O6rCS-ZwU_MWdCzx0CEI_WnyZ2)
- [Jupyter Notebook - Actor network](https://colab.research.google.com/drive/1Lps2fkRlyPAnR63hDOihzCaMvo_RU6Ds)
- [IMDb Datasets](https://developer.imdb.com/non-commercial-datasets/)
- Learn about the [`sknetwork` package](https://scikit-network.readthedocs.io/en/latest/use_cases/votes.html)
- Learn about the [scipy.sparse matrices](https://cmdlinetips.com/2018/03/sparse-matrices-in-python-with-scipy/) and [video](https://youtu.be/v_S7cOL5ZWU)
- [Introduction to Kumu](https://youtu.be/fwiz7PnipgQ)
- [Network analysis with Kumu](https://docs.kumu.io/guides/disciplines/sna-network-mapping)
- [Introduction to Systems and Network Mapping with Kumu](https://www.coursera.org/projects/systems-network-kumu)
