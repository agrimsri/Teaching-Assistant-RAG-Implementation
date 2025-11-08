---
source_url: "https://tds.s-anand.net/#/cors"
---

## CORS: Cross-Origin Resource Sharing

CORS (Cross-Origin Resource Sharing) is a security mechanism that controls how web browsers handle requests between different origins (domains, protocols, or ports). Data scientists need CORS for APIs serving data or analysis to a browser on a different domain.

Watch this practical explanation of CORS (3 min):

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the Image Shows:**
    *   The image is a title card or thumbnail likely for a video or presentation about CORS (Cross-Origin Resource Sharing).
    *   It features prominent text in a stylized, modern design.

2.  **Key Elements, Text, or Data Visible:**
    *   **Text:**
        *   "100 SECONDS OF" (at the top)
        *   "Cors" (large, stylized, in red with a black and white outline)
        *   "CROSS-ORIGIN RESOURCE SHARING" (smaller, bold, white text)
    *   **Colors:** Black, red, white, and gray are the primary colors used.
    *   **Layout:** The text is arranged in a stacked format, with "Cors" as the main focal point.
    *   **Background:** The background consists of a grayscale gradient with subtle white design elements.

3.  **The Purpose or Educational Value:**
    *   The image serves as an introduction to the topic of CORS.
    *   The "100 SECONDS OF" likely indicates that the associated video or presentation will provide a concise explanation of CORS.
    *   It informs viewers that the video will cover the topic of Cross-Origin Resource Sharing.

4.  **Specific Technical Details:**
    *   The image refers to "CORS" which stands for Cross-Origin Resource Sharing.
    *   CORS is a browser security feature that restricts web pages from making requests to a different domain than the one which served the web page.
    *   The title suggests that the presentation will cover the core concepts of CORS.

*Original image: ![CORS in 100 Seconds](https://i.ytimg.com/vi_webp/4KHiSt0oLJ0/sddefault.webp)*](https://youtu.be/4KHiSt0oLJ0)

Key CORS concepts:

- **Same-Origin Policy**: Browsers block requests between different origins by default
- **CORS Headers**: Server responses must include specific headers to allow cross-origin requests
- **Preflight Requests**: Browsers send OPTIONS requests to check if the actual request is allowed
- **Credentials**: Special handling required for requests with cookies or authentication

If you're exposing your API with a GET request publicly, the only thing you need to do is set the HTTP header `Access-Control-Allow-Origin: *`.

Here are other common CORS headers:

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Allow-Credentials: true
```

To implement CORS in FastAPI, use the [`CORSMiddleware` middleware](https://fastapi.tiangolo.com/tutorial/cors/):

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"]) # Allow GET requests from all origins
# Or, provide more granular control:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Allow a specific domain
    allow_credentials=True,  # Allow cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow specific methods
    allow_headers=["*"],  # Allow all headers
)
```

Testing CORS with JavaScript:

```javascript
// Simple request
const response = await fetch("https://api.example.com/data", {
  method: "GET",
  headers: { "Content-Type": "application/json" },
});

// Request with credentials
const response = await fetch("https://api.example.com/data", {
  credentials: "include",
  headers: { "Content-Type": "application/json" },
});
```

Useful CORS debugging tools:

- [CORS Checker](https://cors-test.codehappy.dev/): Test CORS configurations
- Browser DevTools Network tab: Inspect CORS headers and preflight requests
- [cors-anywhere](https://github.com/Rob--W/cors-anywhere): CORS proxy for development

Common CORS errors and solutions:

- `No 'Access-Control-Allow-Origin' header`: Configure server to send proper CORS headers
- `Request header field not allowed`: Add required headers to `Access-Control-Allow-Headers`
- `Credentials flag`: Set both `credentials: 'include'` and `Access-Control-Allow-Credentials: true`
- `Wild card error`: Cannot use `*` with credentials; specify exact origins
