---
source_url: "https://tds.s-anand.net/#/unicode"
---

## Unicode

Ever noticed when you copy-paste some text and get garbage symbols? Or see garbage when you load a CSV file? This video explains why. It covers how computers store text (called character encoding) and why it sometimes goes wonky.

Learn about ASCII (the original 7-bit encoding system that could only handle 128 characters), why that wasn't enough for global languages, and how modern solutions like Unicode save the day by letting us use any character from any language.

Some programs try to guess encodings (sometimes badly!). A signature called BOM (Byte Order Mark)helps computers know exactly how to read text files correctly.

Learn how Unicode, UTF-8 and character encoding works. This is a common gotcha when building apps that handle international text - something bootcamps often skip but developers and data scientists regularly face in the real world.

Unicode is fundamental for data scientists working with international data. Here are key concepts you need to understand:

- **Character Encodings**: Different ways to represent text in computers
  - ASCII (7-bit): Limited to 128 characters, English-only
  - UTF-8: Variable-width encoding, backwards compatible with ASCII
  - UTF-16: Fixed-width encoding, used in Windows and Java
  - UTF-32: Fixed-width encoding, memory inefficient but simple

Common encoding issues you'll encounter:

```python
# Reading files with explicit encoding
with open('file.txt', encoding='utf-8') as f:
    text = f.read()

# Handling encoding errors
import pandas as pd
df = pd.read_csv('data.csv', encoding='utf-8', errors='replace')

# Detecting file encoding
import chardet
with open('unknown.txt', 'rb') as f:
    result = chardet.detect(f.read())
print(result['encoding'])
```

[**[Image Description]**: Here's a detailed description of the image:

**1. What the image shows**

The image is a screen capture from a video, likely a YouTube tutorial, about computer science topics. It features a man in a plaid shirt positioned on the right side of the frame. Behind him and occupying the left portion of the screen is what appears to be a screenshot of computer code, possibly JavaScript, scrolling or presented in a dark theme text editor. The overlay text and layout strongly suggest this is a video thumbnail.

**2. Key elements, text, or data visible**

*   **Text Overlay:** Large, stylized text overlays dominate the image:
    *   "COMPUTER STUFF" - in a prominent, bold font.
    *   "THEY DIDN'T TEACH YOU" - positioned below "COMPUTER STUFF."
    *   "Code Pages, Character Encoding, Unicode, UTF-8 and the BOM" - describing the content of the video.
    *   "PART 2" -  Indicating that this video is part of a series.
*   **Coding Background:** The blurry code snippet in the background contains common JavaScript elements, including:
    *   Function definitions.
    *   Selectors (e.g., "querySelectorAll").
    *   DOM manipulation references ("class").
    *   String operations ("push," "slice," "toLowerCase").
    *   Variables ("length," "name").
*   **Person:** The man is looking at the camera and appears to be speaking. He is wearing a blue and white checkered shirt.

**3. The purpose or educational value**

The image is designed to attract viewers to a video covering fundamental computer science concepts, particularly related to character encoding. The title, "Computer Stuff They Didn't Teach You," suggests the content addresses topics often omitted from standard computer science curricula. The specific topics of Code Pages, Character Encoding, Unicode, UTF-8, and the Byte Order Mark (BOM) indicate the video likely explains how computers represent and handle text in different languages and formats. The "PART 2" label implies this is a continuation of a prior video.

**4. Specific technical details**

The topics listed (Code Pages, Character Encoding, Unicode, UTF-8, BOM) are all critical in software development. Character encoding is how computers map characters to numerical values. Unicode is a universal character encoding standard that aims to include all characters from all writing systems. UTF-8 is a variable-width character encoding for Unicode. Code pages are earlier character encoding standards that are less comprehensive than Unicode. The BOM is a special sequence of bytes at the beginning of a text file that indicates the endianness (byte order) and encoding of the file.

In summary, the image promotes a video about important, yet often under-taught, aspects of character encoding in computer systems. The screenshot with code suggests some programming is involved, and the listed topics denote low-level details about how text data is managed.

*Original image: ![Code Pages, Character Encoding, Unicode, UTF-8 and the BOM - Computer Stuff They Didn't Teach You #2 (17 min)](https://i.ytimg.com/vi_webp/jeIBNn5Y5fI/sddefault.webp)*](https://youtu.be/jeIBNn5Y5fI)
