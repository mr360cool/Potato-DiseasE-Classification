from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os
from pathlib import Path

app = FastAPI()

origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost,http://localhost:3000",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = Path(__file__).resolve().parent.parent / "saved_model" / "1.keras"
MODEL = tf.keras.models.load_model(model_path, compile=False)


CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    # --- CHANGE 3: The loaded model directly returns the prediction tensor ---
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": float(confidence)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
