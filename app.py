import pickle

import numpy as np
import requests
import streamlit as st

from utils.aqi_forecast import fetch_future_air_data
from utils.utils_data import air_content_mean, compare_aqi, plot_air_data


def fetch_aqi(city: str):
    url = "https://aqi-fastapi.herokuapp.com/predict-from-city"
    query = {"city": city}
    response = requests.post(url=url, json=query).json()
    if response is not None:
        aqi = response['AQI']
    else:
        aqi = None
    return aqi

def fetch_aqi_from_air_contents(pm2_5,pm10,no,no2,nh3,co,so2,o3):
    url = "https://aqi-fastapi.herokuapp.com/predict-from-air-contents"
    query = {"pm2_5":pm2_5,"pm10":pm10,"no":no,"no2":no2,"nh3":nh3,"co":co,"so2":so2,"o3":o3}
    response = requests.post(url=url, json=query).json()
    if response is not None:
        aqi = response['AQI']
    else:
        aqi = None
    return aqi
    
if __name__ == "__main__":

    st.title("AQI Prediction")
    st.markdown("---")
    st.markdown("#")
    from datetime import date, timedelta

    city = st.text_input("Enter the city name: ")

    if city:
        data_today, data_first, data_second, data_third, data_fourth, data_fifth, pre_data_first,pre_data_second,pre_data_third, pre_data_fourth, pre_data_fifth = fetch_future_air_data(city)
        if data_today is not None:
            today = date.today()
            today_disp = date.today().strftime("%d-%m-%Y")
            first_day = (today + timedelta(days=1)).strftime("%d-%m-%Y")
            second_day = (today + timedelta(days=2)).strftime("%d-%m-%Y")
            third_day = (today + timedelta(days=3)).strftime("%d-%m-%Y")
            fourth_day = (today + timedelta(days=4)).strftime("%d-%m-%Y")
            fifth_day = (today + timedelta(days=5)).strftime("%d-%m-%Y")

            pre_first_day = (today - timedelta(days=1)).strftime("%d-%m-%Y")
            pre_second_day = (today - timedelta(days=2)).strftime("%d-%m-%Y")
            pre_third_day = (today - timedelta(days=3)).strftime("%d-%m-%Y")
            pre_fourth_day = (today - timedelta(days=4)).strftime("%d-%m-%Y")
            pre_fifth_day = (today - timedelta(days=5)).strftime("%d-%m-%Y")
            
            st.sidebar.subheader("Select the date to get the forecast (for next 5 days)")
            option = st.sidebar.selectbox("Pick a date", (today_disp, first_day, second_day, third_day, fourth_day))
            
            air_content_to_show = st.sidebar.multiselect("Select the air contents", ("co","no","no2","o3","so2","pm2_5","pm10","nh3"))

            button = st.sidebar.button("Submit")

            if button:
                if option == today_disp:
                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for today {today_disp} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(data_today, air_content_to_show)

                    
                elif option == first_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for tomorrow {first_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(data_first, air_content_to_show)


                elif option == second_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {second_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(data_second, air_content_to_show)

                elif option == third_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {third_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(data_third, air_content_to_show)

                elif option == fourth_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {fourth_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(data_fourth, air_content_to_show)
            
                elif option == pre_first_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {pre_first_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(pre_data_first, air_content_to_show)


                elif option == pre_second_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {pre_second_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(pre_data_second, air_content_to_show)

                elif option == pre_third_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {pre_third_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(pre_data_third, air_content_to_show)

                elif option == pre_fourth_day:

                    air_content = air_content_mean(data_today)
                    air_content = list(air_content.values())
                    predicted_aqi = fetch_aqi_from_air_contents(*air_content)
                    st.subheader(f"The forecasted AQI for {pre_fourth_day} is: **{predicted_aqi:.2f}**")
                    st.write("")
                    compare_aqi(predicted_aqi)
                    plot_air_data(pre_data_fourth, air_content_to_show)
                else:
                    st.error("Please enter a valid city name")




