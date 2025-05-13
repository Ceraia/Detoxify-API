# Detoxify Simple API

A lightweight FastAPI wrapper around the [Detoxify](https://github.com/unitaryai/detoxify) library for toxicity detection in text. This API allows you to quickly detect toxic content in text using pre-trained models.

## Overview

This project provides a simple REST API for the Detoxify library, which uses deep learning models to identify toxic content in text. The API can detect various types of toxicity, including:

- Toxicity
- Severe toxicity
- Obscenity
- Threat
- Insult
- Identity-based hate

## Getting Started

### Prerequisites

- Docker and Docker Compose (recommended)
- Python 3.10+ (for local development)

### Running with Docker

The easiest way to run the API is using Docker:

```bash
docker-compose up
```

This will start the API server on port 8000.

### Running Locally

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Start the API server:

```bash
uvicorn toxicity_api:app --host 0.0.0.0 --port 8000
```

## API Usage

### Endpoint

`POST /predict`

### Request Format

```json
{
  "text": "The text you want to analyze for toxicity"
}
```

### Response Format

```json
{
  "toxicity": 0.05,
  "severe_toxicity": 0.01,
  "obscene": 0.02,
  "threat": 0.01,
  "insult": 0.03,
  "identity_hate": 0.01
}
```

The values are probabilities between 0 and 1, where higher values indicate higher likelihood of that category of toxicity.

### Example

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"This is a test message"}'
```

## Project Structure

- `toxicity_api.py` - FastAPI application that serves the toxicity detection endpoint
- `Dockerfile` - Configuration for building the Docker image
- `docker-compose.yml` - Configuration for running the service
- `requirements.txt` - Python dependencies

## Disclaimer

This project is a simple API wrapper around the Detoxify library. All rights to the underlying models, libraries, and resources belong to their respective owners. This project does not claim ownership over any third-party components used, including but not limited to the Detoxify library and its pre-trained models.

- The Detoxify library is developed and maintained by Unitary AI: [https://github.com/unitaryai/detoxify](https://github.com/unitaryai/detoxify)
- FastAPI is developed by Sebastián Ramírez: [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)

## License

Please note that the Detoxify models have their own licensing terms. Refer to the [Detoxify repository](https://github.com/unitaryai/detoxify) for details on model licensing.