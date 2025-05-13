from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel
import os
import sys
import importlib.util
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Global model variable
model = None

def get_or_install_package(package_name):
    """Check if a package is installed, and install it if not."""
    if importlib.util.find_spec(package_name) is None:
        logger.info(f"Installing {package_name}...")
        
        # Ensure pip install goes to the site packages mount point to preserve across restarts
        os.system(f"pip install {package_name} --target=/.cached_packages")
        
        # Add the cached packages directory to the path
        if "/.cached_packages" not in sys.path:
            sys.path.append("/.cached_packages")
        
        logger.info(f"{package_name} installed.")
    else:
        logger.info(f"{package_name} already installed.")

def get_model():
    """Lazy load the model only when needed."""
    global model
    if model is None:
        # Check and install necessary packages
        get_or_install_package("torch")
        get_or_install_package("transformers")
        get_or_install_package("detoxify")
        
        # Now we can import detoxify
        from detoxify import Detoxify
        
        logger.info("Loading detoxify model...")
        model = Detoxify('original')
        logger.info("Model loaded successfully.")
    
    return model

class Input(BaseModel):
    text: str

@app.post("/predict")
async def predict(input: Input):
    # Get or load the model
    model = get_model()
    
    # Make prediction
    raw_result = model.predict(input.text)
    
    # Convert numpy values to Python floats
    result = {key: float(value) for key, value in raw_result.items()}
    
    return result
