---
source_url: "https://tds.s-anand.net/#/live-sessions"
---

# Live Sessions

Live sessions by the instructors and TAs are recorded and uploaded to YouTube.

[**[Image Description]**: Here is a detailed description of the image:

**1. What the image shows:**

The image is a stylized, colorful illustration related to Data Science. It's designed as a rectangular poster with various icons, charts, and diagrams arranged in a visually engaging manner. The icons represent data analysis tools, visualizations, and concepts associated with data science.

**2. Key elements, text, or data visible:**

*   **Text:** "TOOLS IN DATA SCIENCE" is prominently displayed in large, blocky letters.
*   **Icons/Diagrams:**
    *   Circular chart with rings and pointers, possibly indicating a measurement or tuning tool.
    *   Stylized depiction of a tablet or screen with a target-like icon.
    *   A network diagram of connected nodes, representing data processing or machine learning.
    *   Bar charts with colorful blocks, which represent statistical data.
    *   Various types of line graphs and charts which visualize trends and insights.
    *   Laptop screen, symbolizing computational tools
    *   Globe, representing global data
    *   Padlock, representing Data security

**3. The purpose or educational value:**

The image serves as a visual overview of the tools and concepts related to data science. It's intended to be informative and educational, providing a quick glimpse into the diverse range of elements involved in this field. It could be used to introduce data science to beginners, or as a visual aid for presenting the topic.

**4. Any specific technical details:**

The image is illustrative and uses simplified representations rather than precise technical depictions. The color palette is vibrant and modern, likely intended to appeal to a broad audience. The image uses geometric shapes and flat design to create a modern, appealing visual.

*Original image: ![TDS Live Sessions: Jan 2025](https://i.ytimg.com/vi_webp/VTBwpPT3A3U/sddefault.webp)*](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

These were downloaded using [yt-dlp](https://github.com/yt-dlp/yt-dlp). The options compress the audio optimized for speech.

```bash
yt-dlp --extract-audio --audio-format opus --embed-thumbnail --postprocessor-args \
  "-c:a libopus -b:a 12k -ac 1 -application voip -vbr off -ar 8000 -cutoff 4000 -frame_duration 60 -compression_level 10" \
  $YOUTUBE_URL
```

They were then transcribed by Gemini 1.5 Flash 002 (currently the best model from a price-quality perspective for audio transcription).

System prompt:

```
You are an expert transcriber of data science audio tutorials
```

User prompt:

```
Transcribe this audio tutorial about Tools in Data Science (TDS) as an FAQ.
Summarize the student questions faithfully.
Summarize the answers succinctly, without missing information, in a conversational style.
Avoid repeating questions, consolidating similar ones.
Prefer "You" and "I" instead of "student" and "instructor".
For example:

**Q1: [Concisely framed question]**

**A1:** [Succinct answer]
```
