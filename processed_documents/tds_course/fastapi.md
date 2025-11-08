---
source_url: "https://tds.s-anand.net/#/fastapi"
---

## Web Framework: FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern Python web framework for building APIs with automatic interactive documentation. It's fast, easy to use, and designed for building production-ready REST APIs.

Here's a minimal FastAPI app, `app.py`:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Run this with `uv run app.py`.

1. **Handle errors by raising HTTPException**

   ```python
   from fastapi import HTTPException

   async def get_item(item_id: int):
       if not valid_item(item_id):
           raise HTTPException(
               status_code=404,
               detail=f"Item {item_id} not found"
           )
   ```

2. **Use middleware for logging**

   ```python
   from fastapi import Request
   import time

   @app.middleware("http")
   async def add_timing(request: Request, call_next):
       start = time.time()
       response = await call_next(request)
       response.headers["X-Process-Time"] = str(time.time() - start)
       return response
   ```

Tools:

- [FastAPI CLI](https://fastapi.tiangolo.com/tutorial/fastapi-cli/): Project scaffolding
- [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation
- [SQLModel](https://sqlmodel.tiangolo.com/): SQL databases
- [FastAPI Users](https://fastapi-users.github.io/): Authentication

Watch this FastAPI Course for Beginners (64 min):

[**[Image Description]**: Here's a detailed description of the image:

1.  **What the image shows:** The image is a thumbnail for a video tutorial. It features a dark blue background that gradients to a lighter shade of blue towards the top.

2.  **Key elements, text, or data visible:**
    *   A white symbol enclosed in parenthesis is in the top-left corner.
    *   The words "FastAPI" are written in teal, with the FastAPI logo of a teal circle with a white lightning bolt inside it on the left.
    *   Below "FastAPI," the words "Crash Course" are written in white and in a larger font size, to emphasize the nature of the content.
    *   The context information "FastAPI Course for Beginners (64 min)" is provided.

3.  **The purpose or educational value:** The image promotes a tutorial on FastAPI, a modern, high-performance web framework for building APIs with Python. The "Crash Course" title suggests it's designed for quick learning. The "(64 min)" indicates the video's length, allowing viewers to gauge the commitment required.

4.  **Specific technical details:** FastAPI is a framework known for its speed, ease of use, automatic data validation, and support for generating API documentation (using OpenAPI and JSON Schema). The video is likely to provide an introduction to using FastAPI to build web APIs.

*Original image: ![FastAPI Course for Beginners (64 min)](https://i.ytimg.com/vi_webp/tLKKmouUams/sddefault.webp)*](https://youtu.be/tLKKmouUams)
