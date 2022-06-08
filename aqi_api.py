import pickle

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

from utils.aqi_forecast import fetch_future_air_data
from utils.utils_data import air_content_mean

app = FastAPI()

class AQIDtypes(BaseModel):
    city: str


@app.post('/predict')
async def predict_api(city: AQIDtypes):

    loaded_model = pickle.load(open("models/aqi_rf.pkl", 'rb'))
    data_today, data_first, data_second, data_third, data_fourth, data_fifth, pre_data_first,pre_data_second,pre_data_third, pre_data_fourth, pre_data_fifth = fetch_future_air_data(city)
    data_dict = air_content_mean(data_today)
    air_contents = list(data_dict.values())
    predicted_aqi = loaded_model.predict(np.array([air_contents]))[0]
    return {
        "AQI": predicted_aqi,
        **data_dict
    }