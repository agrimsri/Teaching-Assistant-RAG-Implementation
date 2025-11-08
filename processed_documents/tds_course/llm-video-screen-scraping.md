---
source_url: "https://tds.s-anand.net/#/llm-video-screen-scraping"
---

## LLM Video Screen-Scraping

Video screen-scraping with LLMs is a powerful technique for extracting structured data from screen recordings. This approach works with any visible screen content and bypasses traditional web scraping limitations like authentication or anti-scraping measures.

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image shows a screen capture featuring two primary sections. The left portion displays the Google AI Studio interface in a web browser, while the right portion shows a video feed of a person, Anand Subramanian, likely from a video conference. The Google AI Studio screen is the main focus, displaying a prompt being constructed for a Gemini model.

2.  **Key elements, text, or data visible:**
    *   **Google AI Studio Interface:** The interface title is "Google AI Studio" with an "Untitled prompt" at the top, indicating a workspace within Google's AI development environment. A sidebar on the left includes options such as "Get API key," "Create new prompt," "New tuned model," "My Library," "Developer documentation," and "Gemini API for Enterprise."
    *   **Prompt and Model Settings:** The main panel of the Google AI Studio interface displays a "System Instructions" box, suggesting a field for defining how the model should behave. A user prompt is visible, requesting "Extract all the information in these tweets as JSON." Below this, the model's response is partially visible: "Okay, here is the information contained in the tweets shown in { }."
    *   **Model Configuration:** On the right of the Google AI Studio interface, there are "Run Settings" and "Result" tabs. The "Model" is set to "Gemini 1.5 Pro 002." Additional options include "Token Count," "Temperature" (set to 1), "JSON mode" (set to "Strict"), "Code Execution," "Function calling," "Grounding," "Advanced settings," and "Safety settings."
    *   **Tweet:** A tweet by user 'Team Veer' is shown in the prompt section. The tweet reads "🚀 Super excited for the launch of the first blockchain in $AVAX ecosystem built by @avaxstars @karmacoinava 💫🚀 🔗karmacoin.ava.money #KARMACOINAVA #AVAX #CRYPTO."
    *   **Video Feed:** The right side shows Anand Subramanian in a video feed. A sign or board behind him is partially visible, containing the text "Data-Fuelled..."

3.  **The purpose or educational value:** The image appears to document a demonstration or tutorial on how to use Google AI Studio with the Gemini model for extracting information from tweets and converting it into a JSON format. It illustrates the process of crafting a prompt, setting model parameters (like temperature and JSON mode), and viewing the model's response. The image suggests a practical application of AI in data extraction and transformation.

4.  **Specific technical details:**
    *   The Gemini 1.5 Pro model is being used.
    *   The user is setting the temperature to 1, indicating a balance between randomness and determinism in the model's output.
    *   The "JSON mode" is set to strict, likely to enforce that the output is a valid JSON object.
    *   The task involves extracting relevant data from a social media post (a tweet) and restructuring it into a structured JSON format.
    *   The image context indicates the tutorial is regarding 'Screen Scraping with Gemini'.

In summary, the image depicts a user interface of Google AI Studio where a user is demonstrating how to extract information from a tweet and convert it into JSON format, using the Gemini 1.5 Pro model with specific settings. The video feed on the right shows Anand Subramanian, likely the instructor or presenter of this tutorial.

*Original image: ![Screen Scraping with Gemini](https://i.ytimg.com/vi_webp/2G1LqS6qO5s/sddefault.webp)*](https://youtu.be/2G1LqS6qO5s)

Key benefits:

- No setup cost or authentication handling
- Works with any visible screen content
- Full control over data exposure
- Extremely cost-effective (< $0.001 per short video)
- Bypasses anti-scraping measures
- Handles varying formats and layouts

### Quick Start Example

Here's a basic workflow using Google's AI Studio and Gemini:

1. **Record the Screen**
   - Use QuickTime (Mac) or Windows Game Bar (Windows), Screen2Gif, or any tool of your choice
   - Select specific screen area containing target data
   - Record scrolling/clicking through content
   - Keep recordings short (30-60 seconds)
2. **Process with Gemini**
   - Upload to [Google AI Studio](https://makersuite.google.com/app/prompts)
   - Select Gemini 1.5 Flash (cost-effective)
   - Prompt for structured output (JSON/CSV)

Example prompt for extracting tabular data:

```text
Turn this video into a JSON array where each item has:
{
  "date": "yyyy-mm-dd",
  "amount": float
}
```

### Cost Calculation

Gemini 1.5 Flash pricing (as of January 2025):

- $0.075 per million tokens
- Cost per frame ~ 250 tokens
- Cost for 24 hours of video at 1 frame per second ~ $1.62!

### Best Practices

1. **Recording Quality**
   - Frame only relevant content
   - Pause briefly on important data
   - Maintain consistent scroll speed
   - Use high contrast display settings
2. **Data Validation**
   - Always verify critical data manually
   - Use spot-checking for large datasets
   - Consider running multiple passes
   - Log and review any anomalies
3. **Error Handling**
   - Request data in simple formats (CSV/JSON)
   - Include validation in prompts
   - Split long videos into segments
   - Handle missing/partial data gracefully

### Use Cases

1. **Data Extraction**
   - Email content aggregation
   - Dashboard metrics collection
   - Protected web content
   - Legacy system data
2. **Data Journalism**
   - Public records analysis
   - Time-series data collection
   - Interactive visualization data
   - Government website scraping
3. **Business Intelligence**
   - Competitor pricing analysis
   - Market research data
   - Internal system migration
   - Legacy report conversion

Tools:

- [Google AI Studio](https://aistudio.google.com/app/prompts): Process videos with Gemini
- [QuickTime Player](https://support.apple.com/guide/quicktime-player/welcome/mac): Screen recording (Mac)
- [Screen2Gif](https://www.screentogif.com/): Screen recording (Windows)
- [OBS Studio](https://obsproject.com/): Advanced screen recording (cross-platform)

References:

- [Simon Willison's Video Scraping Tutorial](https://simonwillison.net/2024/Oct/17/video-scraping/)
- [Gemini API Documentation](https://ai.google.dev/docs)
