---
source_url: "https://tds.s-anand.net/#/function-calling"
---

## Function Calling with OpenAI

[Function Calling](https://platform.openai.com/docs/guides/function-calling) allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and AI assistants that need to interact with your backend systems.

OpenAI supports [Function Calling](https://platform.openai.com/docs/guides/function-calling) -- a way for LLMs to suggest what functions to call and how.

[**[Image Description]**: Here's a detailed description of the image:

**1. What the image shows:**

The image is a screenshot from what appears to be a YouTube tutorial or educational video on OpenAI Function Calling. The image combines a person in the foreground with a code editor (likely VS Code) in the background displaying a Python script. There's a large red arrow pointing at a specific section of the code in the editor. The background is a gradient of blue to black, and bold text overlays the top of the image.

**2. Key elements, text, or data visible:**

*   **Foreground:** A man with short, curly hair, wearing a black turtleneck sweater and an Apple Watch is positioned on the left side of the image. He has his hand raised towards the code editor.
*   **Text Overlay:** The bold text "FUNCTIONS EXPLAINED" is prominent at the top of the image, indicating the topic of the tutorial.
*   **Code Editor:** The right side of the image features a code editor window, showcasing a Python script. The script appears to be related to Langchain and involves OpenAI Function Calling.
*   **Code Snippet:** The code snippet focuses on defining a function named "get\_flight\_info" with parameters "loc\_origin" and "loc\_destination." The description explains that the function is designed to retrieve flight information between two locations. It specifies that both "loc\_origin" and "loc\_destination" are required parameters.
*   **Filenames/Paths:** The filename displayed is "openai\_function\_calling.py" which is part of a "langchain-experiments" project. The file path indicates that the file is located within an "openai-functions" folder.
*   **Bottom Bar of Code Editor:** The bottom bar of the code editor shows indicators like "Spaces: 4," "UTF-8," "LF," and "Python 3.10.11."

**3. The purpose or educational value:**

The purpose of the image is educational. It's designed to provide a tutorial or explanation of OpenAI Function Calling. The code snippet highlights how to define functions and their parameters within a Langchain context. The person in the foreground serves as the presenter or instructor guiding the viewer through the process.

**4. Specific technical details:**

*   The code is written in Python and uses a dictionary structure to define function parameters and their descriptions.
*   The "loc\_origin" and "loc\_destination" parameters are both strings and have descriptions specifying that they represent airport codes (e.g., DUS, HAM).
*   The code snippet implies the use of Langchain, a library for building language model applications, to interact with OpenAI models.

In summary, this image represents a tutorial on OpenAI Function Calling within a Langchain environment, focusing on how to define functions and their parameters in Python.

*Original image: ![OpenAI Function Calling - Full Beginner Tutorial](https://i.ytimg.com/vi_webp/aqdWSYWC_LI/sddefault.webp)*](https://youtu.be/aqdWSYWC_LI)

Here's a minimal example using Python and OpenAI's function calling that identifies the weather in a given location.

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///

import httpx
import os
from typing import Dict, Any


def query_gpt(user_input: str, tools: list[Dict[str, Any]]) -> Dict[str, Any]:
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": user_input}],
            "tools": tools,
            "tool_choice": "auto",
        },
    )
    return response.json()["choices"][0]["message"]


WEATHER_TOOL = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name or coordinates"}
            },
            "required": ["location"],
            "additionalProperties": False,
        },
        "strict": True,
    },
}

if __name__ == "__main__":
    response = query_gpt("What is the weather in San Francisco?", [WEATHER_TOOL])
    print([tool_call["function"] for tool_call in response["tool_calls"]])
```

### How to define functions

The function definition is a [JSON schema](https://json-schema.org/) with a few OpenAI specific properties.
See the [Supported schemas](https://platform.openai.com/docs/guides/structured-outputs#supported-schemas).

Here's an example of a function definition for scheduling a meeting:

```python
MEETING_TOOL = {
    "type": "function",
    "function": {
        "name": "schedule_meeting",
        "description": "Schedule a meeting room for a specific date and time",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Meeting date in YYYY-MM-DD format"
                },
                "time": {
                    "type": "string",
                    "description": "Meeting time in HH:MM format"
                },
                "meeting_room": {
                    "type": "string",
                    "description": "Name of the meeting room"
                }
            },
            "required": ["date", "time", "meeting_room"],
            "additionalProperties": False
        },
        "strict": True
    }
}
```

### How to define multiple functions

You can define multiple functions by passing a list of function definitions to the `tools` parameter.

Here's an example of a list of function definitions for handling employee expenses and calculating performance bonuses:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_expense_balance",
            "description": "Get expense balance for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    }
                },
                "required": ["employee_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_performance_bonus",
            "description": "Calculate yearly performance bonus for an employee",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_id": {
                        "type": "integer",
                        "description": "Employee ID number"
                    },
                    "current_year": {
                        "type": "integer",
                        "description": "Year to calculate bonus for"
                    }
                },
                "required": ["employee_id", "current_year"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]
```

Best Practices:

1. **Use Strict Mode**
   - Always set `strict: True` to ensure valid function calls
   - Define all required parameters
   - Set `additionalProperties: False`
2. **Use tool choice**
   - Set `tool_choice: "required"` to ensure that the model will always call one or more tools
   - The default is `tool_choice: "auto"` which means the model will choose a tool only if appropriate
3. **Clear Descriptions**
   - Write detailed function and parameter descriptions
   - Include expected formats and units
   - Mention any constraints or limitations
4. **Error Handling**
   - Validate function inputs before execution
   - Return clear error messages
   - Handle missing or invalid parameters
