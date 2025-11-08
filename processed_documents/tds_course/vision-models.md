---
source_url: "https://tds.s-anand.net/#/vision-models"
---

## Vision Models

[**[Image Description]**: Here is a detailed description of the image:

1.  **Image Content:** The image displays a screen capture of a Windows desktop. The main focus is a window displaying a photograph of a cricket player in a blue jersey with "INDIA" emblazoned on the front. The player is holding up a cricket bat and helmet. A file explorer window is visible behind the image, showing a list of JPEG files. A man is present in the lower-right corner, appearing to be recording or participating in a video call.

2.  **Key Elements and Text:**
    *   **Cricket Player:** The prominent element is the cricket player, wearing a blue India jersey and holding up his bat and helmet in a celebratory gesture.
    *   **File Explorer Window:** This window displays a list of files, including "cricket.jpg" and other JPEG files, with columns for "Name," "Path," "Size," and "Date Modified."
    *   **File Path:** The path of the image being displayed is "C:\Users\Pattie Oye - People - Documents\People\Government\People Strategy\People Initiatives\Culture\Great Place to Work\WorldGrammacee Solutions\Shared drive\rentis Opz - People\Shared Documents\People\Government\People Strategy\People Initiatives\Culture\Great Place to Work\Kabeen\Kartut Khirat Place..."
    *   **Image Dimensions and Size:** The image of the cricket player has dimensions of 1306x675 and a file size of 76.3 KB, as indicated on the image viewer.
    *   **User Interface:** Visible is the standard Windows user interface including the Start Menu, taskbar, and window controls (minimize, maximize, close). Icons of different programs are visible on the taskbar.
    *   **Text in UI:** There are text elements from the Windows user interface like "File," "Edit," "View," "Search," "Bookmarks," "Tools," and "Help" on the top menu. Text indicating the size and date modified are also visible for the listed files.
    *   **Man:** A man is visible in the bottom right corner of the screenshot.

3.  **Purpose and Educational Value:**
    *   This image demonstrates a person presumably looking at images on their computer, which could be for presentation or training purposes.
    *   It shows how to use file explorer in Windows to navigate and open images.
    *   The file path displayed gives context to the origin and organization of files on a Windows system.

4.  **Specific Technical Details:**
    *   The image is captured from a Windows operating system.
    *   The file explorer window indicates a hierarchical file system structure and file metadata.
    *   The image viewer indicates basic functionalities such as zoom level (97%).
    *   The taskbar indicates the presence of the Run command.

*Original image: ![LLM Vision Models](https://i.ytimg.com/vi_webp/FgT_Mk_bakQ/sddefault.webp)*](https://youtu.be/FgT_Mk_bakQ)

You'll learn how to use LLMs to interpret images and extract useful information, covering:

- **Setting Up Vision Models**: Integrate vision capabilities with LLMs using APIs like OpenAI's Chat Completion.
- **Sending Image URLs for Analysis**: Pass URLs or base64-encoded images to LLMs for processing.
- **Reading Image Responses**: Get detailed textual descriptions of images, from scenic landscapes to specific objects like cricketers or bank statements.
- **Extracting Data from Images**: Convert extracted image data to various formats like Markdown tables or JSON arrays.
- **Handling Model Hallucinations**: Address inaccuracies in extraction results, understanding how different prompts can affect output quality.
- **Cost Management for Vision Models**: Adjust detail settings (e.g., "detail: low") to balance cost and output precision.

Here are the links used in the video:

- [Jupyter Notebook](https://colab.research.google.com/drive/1bK0b1XMrZWImtw01T1w9NGraDkiVi8mS)
- [OpenAI Chat API Reference](https://platform.openai.com/docs/api-reference/chat/create)
- [OpenAI Vision Guide](https://platform.openai.com/docs/guides/vision)
- [Sample images used](https://drive.google.com/drive/folders/14MFc7XmGIUDU4-vbmF9305c1SSQrM-gR)

Here is an example of how to analyze an image using the OpenAI API.

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What is in this image?"},
          {
            "type": "image_url",
            "detail": "low",
            "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Correlation_coefficient.png"}
          }
        ]
      }
    ]
  }'
```

Let's break down the request:

- `curl https://api.openai.com/v1/chat/completions`: The API endpoint for text generation.
- `-H "Content-Type: application/json"`: The content type of the request.
- `-H "Authorization: Bearer $OPENAI_API_KEY"`: The API key for authentication.
- `-d`: The request body.
  - `"model": "gpt-4o-mini"`: The model to use for text generation.
  - `"messages":`: The messages to send to the model.
    - `"role": "user"`: The role of the message.
    - `"content":`: The content of the message.
      - `{"type": "text", "text": "What is in this image?"}`: The text message.
      - `{"type": "image_url"}`: The image message.
        - `"detail": "low"`: The detail level of the image. `low` uses fewer tokens at lower detail. `high` uses more tokens for higher detail.
        - `"image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/3/34/Correlation_coefficient.png"}`: The URL of the image.

You can send images in a [base64 encoded format](base64-image.md), too. For example:

```bash
# Download image and convert to base64 in one step
IMAGE_BASE64=$(curl -s "https://upload.wikimedia.org/wikipedia/commons/3/34/Correlation_coefficient.png" | base64 -w 0)

# Send to OpenAI API
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d @- << EOF
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What is in this image?"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,$IMAGE_BASE64" }
        }
      ]
    }
  ]
}
EOF
```
