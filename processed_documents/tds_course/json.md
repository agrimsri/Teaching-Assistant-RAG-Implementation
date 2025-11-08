---
source_url: "https://tds.s-anand.net/#/json"
---

## JSON

JSON (JavaScript Object Notation) is the de facto standard format for data exchange on the web and APIs. Its human-readable format and widespread support make it essential for data scientists working with web services, APIs, and configuration files.

For data scientists, JSON is essential when:

- Working with REST APIs and web services
- Storing configuration files and metadata
- Parsing semi-structured data from databases like MongoDB
- Creating data visualization specifications (e.g., Vega-Lite)

Watch this comprehensive introduction to JSON (15 min):

[**[Image Description]**: Here's a detailed description of the image:

**1. What the Image Shows:**

The image is a screen capture, likely from a video or tutorial, focusing on JSON (JavaScript Object Notation). It visually represents the concept of JSON and its structure using code examples and text overlays.

**2. Key Elements, Text, or Data Visible:**

*   **JSON Code:** The main part of the image displays JSON code with key-value pairs. Examples include:
    *   `"name": "Big Corporation"`
    *   `"employee": 0000`
    *   `"ceo": null`
    *   `"rating": 4.3`
*   **Text Overlay:** The word "JSON" is prominently displayed in large, green, stylized lettering over the code.  The text "Crash Course" is also present in a smaller, bolder font and a green bar, placed below the "JSON" text.
*   **Code Editor:** The background resembles a code editor, indicating this is a programming-related concept. Line numbers (e.g., 2, 3, 4, 5, 6, 7, 8, 11, 12) are visible to the left of the code.
*   **Logo:** A small, circular logo with a flame symbol is in the upper left corner.

**3. The Purpose or Educational Value:**

The image appears to be designed to introduce or teach about JSON. The term "Crash Course" implies a quick, introductory tutorial on the topic. The presence of sample JSON code helps viewers understand the syntax and structure of JSON data.

**4. Specific Technical Details:**

*   **JSON Structure:** The JSON code demonstrates the use of key-value pairs, where keys are strings (within double quotes) and values can be strings, numbers, booleans, or even `null`.
*   **Data Types:** The examples in the code use different JSON data types:
    *   String (e.g., "Big Corporation")
    *   Number (e.g., 0000, 4.3)
    *   Null (e.g., null)
*   **Code editor theme:** The theme applied to the code editor is using dark colors with light syntax highlighting.

*Original image: ![JSON Crash Course](https://i.ytimg.com/vi_webp/GpOO5iKzOmY/sddefault.webp)*](https://youtu.be/GpOO5iKzOmY)

Key concepts to understand in JSON:

- JSON only supports 6 data types: strings, numbers, booleans, null, arrays, and objects
- You can nest data. Arrays and objects can contain other data types, including other arrays and objects
- Always validate. Ensure JSON is well-formed. Comm errors: Trailing commas, missing quotes, and escape characters

[JSON Lines](https://jsonlines.org/) is a format that allows you to store multiple JSON objects in a single line.
It's useful for logging and streaming data.

Tools you could use with JSON:

- [JSONLint](https://jsonlint.com/): Validate and format JSON
- [JSON Editor Online](https://jsoneditoronline.org/): Visual JSON editor and formatter
- [JSON Schema](https://json-schema.org/): Define the structure of your JSON data
- [jq](https://stedolan.github.io/jq/): Command-line JSON processor

Common Python operations with JSON:

```python
import json

# Parse JSON string
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)

# Convert to JSON string
json_str = json.dumps(data, indent=2)

# Read JSON from file
with open('data.json') as f:
    data = json.load(f)

# Write JSON to file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read JSON data a Pandas DataFrame. JSON data is typically stored as an array of objects.
import pandas as pd
df = pd.read_json('data.json')

# Read JSON lines from file into a DataFrame. JSON lines are typically one line per object.
df = pd.read_json('data.jsonl', lines=True)
```

Practice JSON skills with these resources:

- [JSON Generator](https://json-generator.com/): Create sample JSON data
- [JSON Path Finder](https://jsonpathfinder.com/): Learn to navigate complex JSON structures
- [JSON Schema Validator](https://www.jsonschemavalidator.net/): Validate JSON against schemas
