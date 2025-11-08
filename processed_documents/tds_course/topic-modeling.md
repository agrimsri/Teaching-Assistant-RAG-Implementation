---
source_url: "https://tds.s-anand.net/#/topic-modeling"
---

## Topic Modeling

[**[Image Description]**: Here's a comprehensive description of the image:

**1. What the Image Shows:**

The image is a screenshot of a Google Colab notebook session during what appears to be a coding tutorial or presentation, captured within a video conferencing environment. The Colab notebook is focused on "Embeddings," likely for a language model (LLM) project. The right side of the image displays a video conference window, showing multiple participants engaged in the session.

**2. Key Elements, Text, and Data Visible:**

*   **Google Colab Interface:** The primary focus is the Colab notebook, displaying:
    *   **Notebook Name:** "Embeddings.ipynb"
    *   **Code Cells:**
        *   One code cell is visible, containing Python code.
            *   It initializes `words` with a list of strings: `['Apple', 'Orange', 'Banana', 'Jamaica', 'Sri Lanka', 'Facebook']`. These appear to be examples for the language model.
            *   It defines `topics` as `['Fruit', 'Country', 'Company']`.
            *   The code then imports `requests` and `json` libraries.
            *   A URL for OpenAI's embeddings API (`https://api.openai.com/v1/embeddings`) is assigned to a variable.
            *   Headers for the API request are defined, including `Authorization` with a "Bearer" token (partially obscured) and `Content-Type` set to `application/json`.
            *   Data for the API request is prepared, including `input` (the `words` list), `model` ("text-embedding-ada-002"), and `encoding_format` ("float").
            *   The code uses the `requests` library to make a POST request to the OpenAI API, sending the data as JSON.
            *   Finally, it prints the JSON response from the API.
    *   **Secrets Panel:** A sidebar displays a "Secrets" management panel, likely for securely storing API keys. It lists secrets such as:
        *   `LLMFOUNDRY_`
        *   `LLMPROXY_JW`
        *   `OPENAI_API_KE`
        *   `huggingface`
        *   `wandb`
        *   `OPENAI_API_KE` (appears to be a duplicate entry)
    *   **Secret Access Instructions:** Text is visible indicating how to access these secret keys in Python using `from google.colab import userdata` and `userdata.get('secretName')`.
*   **Video Conference Participants:**
    *   Multiple individuals are visible in the video conference on the right side of the screen. Their names appear to be:
        *   Dibo John Philip
        *   Anand S
        *   Anit
*   **Status Bar:** At the bottom of the Colab interface, it indicates that the cell execution has "completed" in "0s" at "12:18PM."
*   **Browser Tabs:** The title bar of the Chrome browser shows tabs labeled:
    *   "Embeddings.ipynb - Colab"
    *   "Embedding projection - visualization"
    *   "API Reference - OpenAI API"
    *   "ChatGPT"

**3. Purpose and Educational Value:**

The image demonstrates a practical application of language model embeddings within a Colab notebook. Its educational value comes from:

*   **API Integration:** Showing how to interact with a third-party API (OpenAI) to generate embeddings.
*   **Secret Management:** Highlighting the importance of securely managing API keys using Colab's secrets feature.
*   **Code Snippets:** Providing working code snippets for tasks like making API requests, handling JSON data, and accessing secret credentials.
*   **Contextual Learning:** Illustrating the workflow of developing an LLM-based application within a Colab environment.

**4. Specific Technical Details:**

*   **OpenAI API:** The code interacts with the OpenAI Embeddings API (`v1/embeddings`).
*   **text-embedding-ada-002:** The specified model is the "text-embedding-ada-002", which is a commonly used model for generating text embeddings.
*   **JSON Format:** The data is formatted as JSON for sending to the API, and the response is expected to be in JSON format as well.
*   **Python Libraries:** The code uses the `requests` library for making HTTP requests and the `json` library for handling JSON data.
*   **Colab's Secrets Feature:** Colab's feature for securely storing API keys, protecting them from being exposed in the notebook itself is being used.

In summary, the image captures a coding session focused on using OpenAI's Embeddings API within Google Colab, with a focus on security and best practices. It would be useful for anyone learning about language models, API integration, or cloud-based coding environments.

*Original image: ![LLM Topic Modeling](https://i.ytimg.com/vi_webp/eQUNhq91DlI/sddefault.webp)*](https://youtu.be/eQUNhq91DlI)

You'll learn to use text embeddings to find text similarity and use that to create topics automatically from text, covering:

- **Embeddings**: How large language models convert text into numerical representations.
- **Similarity Measurement**: Understanding how similar embeddings indicate similar meanings.
- **Embedding Visualization**: Using tools like Tensorflow Projector to visualize embedding spaces.
- **Embedding Applications**: Using embeddings for tasks like classification and clustering.
- **OpenAI Embeddings**: Using OpenAI's API to generate embeddings for text.
- **Model Comparison**: Exploring different embedding models and their strengths and weaknesses.
- **Cosine Similarity**: Calculating cosine similarity between embeddings for more reliable similarity measures.
- **Embedding Cost**: Understanding the cost of generating embeddings using OpenAI's API.
- **Embedding Range**: Understanding the range of values in embeddings and their significance.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/15L075RLrwXkxa29EGT-1sNm_dqJRBTe_)
- [Tensorflow projector](https://projector.tensorflow.org/)
- [Embeddings guide](https://platform.openai.com/docs/guides/embeddings)
- [Embeddings reference](https://platform.openai.com/docs/api-reference/embeddings)
- [Clustering on scikit-learn](https://scikit-learn.org/stable/modules/clustering.html)
- [Massive text embedding leaderboard (MTEB)](https://huggingface.co/spaces/mteb/leaderboard)
- [`gte-large-en-v1.5` embedding model](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5)
- [Embeddings similarity threshold](https://www.s-anand.net/blog/embeddings-similarity-threshold/)
