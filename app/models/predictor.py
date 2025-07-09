# import pandas as pd
# import numpy as np
# from keras.models import load_model

# MODEL_PATH = "model/traffic_model.h5"

# class TrafficModel:
#     def __init__(self):
#         self.model = load_model(MODEL_PATH)

#     def predict(self, input_data: dict) -> dict:
#         df = pd.DataFrame([input_data])
#         prediction = self.model.predict(df)[0]  # get 1D output array
#         return {
#             "green_time_N": float(prediction[0]),
#             "green_time_S": float(prediction[1]),
#             "green_time_E": float(prediction[2]),
#             "green_time_W": float(prediction[3])
#         }



import pandas as pd
import numpy as np
import pickle
from keras.models import load_model

MODEL_PATH = "model/traffic_model.h5"
IN_SCALER_PATH = "model/morning_time_scaler_independent.pkl"
OUT_SCALER_PATH = "model/morning_time_scaler_dependent.pkl"

class TrafficModel:
    def __init__(self):
        self.model = load_model(MODEL_PATH)

        # Load scalers
        with open(IN_SCALER_PATH, "rb") as f:
            self.in_scaler = pickle.load(f)
        with open(OUT_SCALER_PATH, "rb") as f:
            self.out_scaler = pickle.load(f)

    def predict(self, input_data: dict) -> dict:
        df = pd.DataFrame([input_data])

        # Scale input
        input_scaled = self.in_scaler.transform(df)

        # Predict
        prediction_scaled = self.model.predict(input_scaled)

        # Inverse scale output
        prediction = self.out_scaler.inverse_transform(prediction_scaled)[0]

        return {
            "green_time_N": float(prediction[0]),
            "green_time_S": float(prediction[1]),
            "green_time_E": float(prediction[2]),
            "green_time_W": float(prediction[3]),
        }
