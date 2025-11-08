---
source_url: "https://tds.s-anand.net/#/image-compression"
---

## Images: Compression

Image compression is essential when deploying apps. Often, pages have dozens of images. Image analysis runs over thousands of images. The cost of storage and bandwidth can grow over time.

Here are things you should know when you're compressing images:

- **Image dimensions** are the width and height of the image in pixels. This impacts image size a lot
- **Lossless** compression (PNG, WebP) preserves exact data
- **Lossy** compression (JPEG, WebP) removes some data for smaller files
- **Vector** formats (SVG) scale without quality loss
- **WebP** is the modern standard, supporting both lossy and lossless

Here's a rule of thumb you can use as of 2025.

- Use SVG if you can (i.e. if it's vector graphics or you can convert it to one)
- Else, reduce the image to as small as you can, and save as lossy WebP

Common operations with Python:

```python
from pathlib import Path
from PIL import Image
import io

async def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Optimize for web
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

# Batch process images
paths = Path('images').glob('*.jpg')
for p in paths:
    await compress_image(p, p.with_suffix('.webp'))
```

Command line tools include [cwebp](https://developers.google.com/speed/webp/docs/cwebp), [pngquant](https://pngquant.org/), [jpegoptim](https://github.com/tjko/jpegoptim), and [ImageMagick](https://imagemagick.org/).

```bash
# Convert to WebP
cwebp -q 85 input.png -o output.webp

# Optimize PNG
pngquant --quality=65-80 image.png

# Optimize JPEG
jpegoptim --strip-all --all-progressive --max=85 image.jpg

# Convert and resize
convert input.jpg -resize 800x600 output.jpg

# Batch convert
mogrify -format webp -quality 85 *.jpg
```

Watch this video on modern image formats and optimization (15 min):

[**[Image Description]**: Here's a detailed description of the image:

1.  **Content Overview:** The image is a screen capture, likely from a video conference or webinar, titled "Image compression deep-dive". It is divided into three sections. The main section on the left features title text along with an illustrated banner. The other two sections feature speakers of the presentation.

2.  **Key Elements:**
    *   **Title:** "Image compression deep-dive" is prominently displayed. The name of the video conference is "web.dev LIVE".
    *   **Illustrations:** At the bottom of the left-hand section is a flat illustration featuring various icons. These icons likely represent elements of web development and image optimization. This includes a potted plant, a heart in a picture, a globe, a laptop with code, a cup of coffee, play buttons, and avatars.
    *   **Speakers:** The right side shows two presenters in separate frames, likely in different locations. Both are young men. The one on top is wearing a blue crewneck shirt. The one at the bottom is also wearing a blue crewneck shirt and a baseball hat.

3.  **Purpose and Educational Value:** The image promotes a session or video related to image compression. The session will likely provide in-depth information about image compression techniques, best practices, and potentially how to improve website performance by optimizing images.

4.  **Specific Technical Details:** While the image itself does not reveal specific technical details, the title indicates that the session is focused on "image compression". This likely covers topics such as:
    *   Image file formats (JPEG, PNG, WebP, AVIF, etc.)
    *   Lossy vs. lossless compression
    *   Compression algorithms
    *   Image optimization tools and techniques
    *   Impact of image compression on website loading speed and user experience

*Original image: ![Modern Image Optimization (15 min)](https://i.ytimg.com/vi_webp/F1kYBnY6mwg/sddefault.webp)*](https://youtu.be/F1kYBnY6mwg)

Tools for image optimization:

- [squoosh.app](https://squoosh.app/): Browser-based compression
- [ImageOptim](https://imageoptim.com/): GUI tool for Mac
- [sharp](https://sharp.pixelplumbing.com/): Node.js image processing
- [Pillow](https://python-pillow.org/): Python imaging library
