import pickle
import uvicorn

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

from utils.aqi_forecast import fetch_future_air_data
from utils.utils_data import air_content_mean

app = FastAPI()

class AQIDtypes(BaseModel):
    city: str

@app.get("/")
def home():
    return {"Welcome to AQI API": "Head on to /predict endpoint or /docs for Swagger UI"}

@app.post("/predict")
async def predict_aqi(city: AQIDtypes = None):
    data_today, data_first, data_second, data_third, data_fourth, data_fifth, pre_data_first,pre_data_second,pre_data_third, pre_data_fourth, pre_data_fifth = fetch_future_air_data(city)
    data_dict = air_content_mean(data_today)
    air_contents = list(data_dict.values())
    loaded_model = pickle.load(open("models/aqi_rf.pkl", 'rb'))
    predicted_aqi = loaded_model.predict(np.array([air_contents]))[0]
    return {
        "AQI": predicted_aqi,
        **data_dict
    }

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)