from pydantic import BaseModel

class TrafficInput(BaseModel):
    vehicles_N: int
    vehicles_S: int
    vehicles_E: int
    vehicles_W: int
    ped_N: int
    ped_S: int
    ped_E: int
    ped_W: int
    emg_N: int
    emg_S: int
    emg_E: int
    emg_W: int