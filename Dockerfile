FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Specifically install the packages needed here to cache this build layer
# and avoid re-installing them if they haven't changed
RUN pip install detoxify transformers torch uvicorn fastapi 

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

COPY detoxify_api.py .

EXPOSE 8000

CMD ["uvicorn", "detoxify_api:app", "--host", "0.0.0.0", "--port", "8000"]
