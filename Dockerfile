# Use a slim Python image compatible with the repo's virtualenv (Python 3.10)
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Create an unprivileged user to run the app
RUN adduser --disabled-password --gecos "" app

WORKDIR /app

# Install system build deps often required by scientific packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       gcc \
       gfortran \
       libatlas-base-dev \
       liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first (cache layer). requirements.txt is in the repo root.
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy the project files
COPY . /app
RUN chown -R app:app /app

# Switch to unprivileged user
USER app

# Expose the port controlled by $PORT (default 5000)
EXPOSE ${PORT}

# Start the FastAPI app using uvicorn. The PORT env var is used by HuggingFace Spaces.
CMD ["sh", "-c", "uvicorn run:app --host 0.0.0.0 --port ${PORT}"]
