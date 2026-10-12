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
loaded_model = tf.keras.models.load_model(model_path, compile=False)
model_input = tf.keras.Input(shape=loaded_model.input_shape[1:])
MODEL = tf.keras.models.clone_model(
    loaded_model,
    input_tensors=model_input,
    recursive=True,
)
MODEL.set_weights(loaded_model.get_weights())
del loaded_model


CLASS_NAMES = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]


@app.get("/ping")
async def ping():
    return "Hello, I am alive"


def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).convert("RGB")
    input_height, input_width = MODEL.input_shape[1:3]
    if input_height is not None and input_width is not None:
        image = image.resize((input_width, input_height))
    return np.asarray(image)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    predictions = MODEL.predict(np.expand_dims(image, 0), verbose=0)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {"class": predicted_class, "confidence": float(confidence)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
