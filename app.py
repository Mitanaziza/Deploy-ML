from string import ascii_uppercase, digits

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
import numpy as np
import cv2
import imutils
import h5py
import uvicorn

app = FastAPI()

# Memuat model
model_path = "model/model1.h5"
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

# Schema input untuk API
class InputData(BaseModel):
    gender: str
    age: int
    height: float
    weight: float


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Port diambil dari variabel lingkungan `PORT`
PORT = int(os.environ.get("PORT", 8000))

# Endpoint utama untuk menghitung BMI dan memprediksi status kesehatan
@app.post("/predict")
async def predict(data: InputData):
    # Validasi input
    if data.gender.lower() not in ["male", "female"]:
        raise HTTPException(status_code=400, detail="Invalid gender. Use 'male' or 'female'.")

    # Hitung BMI
    bmi = data.weight / ((data.height / 100) ** 2)

    # Format input untuk model (sesuaikan dengan kebutuhan model Anda)
    input_array = np.array([[bmi, data.age]])
    
    # Prediksi menggunakan model
    try:
        prediction = model.predict(input_array)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Model prediction failed: {e}")

    # Hasil prediksi
    status = "Healthy" if prediction[0][0] > 0.5 else "Unhealthy"

    return {
        "bmi": round(bmi, 2),
        "health_status": status
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)