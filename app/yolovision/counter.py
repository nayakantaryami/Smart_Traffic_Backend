import cv2
from ultralytics import YOLO

class VehicleCounter:
    def __init__(self, model_path="model/yolov8n.pt"):
        self.model = YOLO(model_path)

    def count_vehicles(self, image_path: str) -> int:
        results = self.model(image_path)[0]
        count = 0
        for cls_id in results.boxes.cls:
            label = int(cls_id)
            if label in [2, 3, 5, 7]:  # car, motorcycle, bus, truck
                count += 1
        return count
