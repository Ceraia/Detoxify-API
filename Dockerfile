FROM python:3.10-slim

WORKDIR /app

# Install only the essential build packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install only the minimal API runtime requirements
RUN pip install --no-cache-dir uvicorn fastapi

# Create directory for cached packages that will be persisted via volume
RUN mkdir -p /.cached_packages

# Add the cached packages directory to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/.cached_packages"

# Copy the API code
COPY detoxify_api.py .

EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "detoxify_api:app", "--host", "0.0.0.0", "--port", "8000"]
