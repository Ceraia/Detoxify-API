from fastapi import FastAPI, Request
from detoxify import Detoxify
from pydantic import BaseModel
import numpy as np

app = FastAPI()
model = Detoxify('original')

class Input(BaseModel):
    text: str

@app.post("/predict")
async def predict(input: Input):
    raw_result = model.predict(input.text)

    result = {key: float(value) for key, value in raw_result.items()}

    return result
