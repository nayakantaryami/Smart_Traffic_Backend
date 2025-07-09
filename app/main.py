# from fastapi import FastAPI
# from app.schemas.input_schema import TrafficInput
# from app.models.predictor import TrafficModel

# app = FastAPI(title="Smart Traffic Management API")
# model = TrafficModel()

# @app.get("/")
# def read_root():
#     return {"message": "Smart Traffic Management System Running"}

# @app.post("/predict")
# def predict_traffic(input_data: TrafficInput):
#     result = model.predict(input_data.dict())
#     return {"prediction": result}






from fastapi import FastAPI, UploadFile, File
from app.schemas.input_schema import TrafficInput
from app.models.predictor import TrafficModel
from app.yolovision.counter import VehicleCounter
import pandas as pd

app = FastAPI(title="Smart Traffic Management API")

# Load ANN model and scalers
model = TrafficModel()

# Load YOLO model
vehicle_counter = VehicleCounter("model/yolov8n.pt")

@app.get("/")
def read_root():
    return {"message": "Smart Traffic Management System Running"}

@app.post("/predict")
def predict_traffic(input_data: TrafficInput):
    result = model.predict(input_data.dict())
    return {"prediction": result}

@app.post("/predict-from-images")
async def predict_from_images(
    north: UploadFile = File(...),
    south: UploadFile = File(...),
    east: UploadFile = File(...),
    west: UploadFile = File(...)
):
    """
    Predict green durations using YOLOv8 vehicle counts from uploaded traffic images.
    """

    # Save uploaded files temporarily
    image_paths = {}
    for direction, file in zip(["N", "S", "E", "W"], [north, south, east, west]):
        path = f"temp_{direction}.jpg"
        with open(path, "wb") as f:
            f.write(await file.read())
        image_paths[direction] = path

    # Count vehicles using YOLO model
    vehicle_counts = {
        f"vehicles_{d}": vehicle_counter.count_vehicles(path)
        for d, path in image_paths.items()
    }

    # Add default pedestrian and emergency values
    vehicle_counts.update({
        "ped_N": 1, "ped_S": 0, "ped_E": 1, "ped_W": 0,
        "emg_N": 1, "emg_S": 0, "emg_E": 0, "emg_W": 0
    })

    # Predict using ANN model with scaled inputs/outputs
    result = model.predict(vehicle_counts)

    return {"prediction": result}
