import streamlit as st
import plotly.express as px

def plot_air_data(data,air_contents):
    """
    Plots air content wrt time
    """
    st.info("💡 All the air contents are in micro-gram per meter-cube")
    # for air_content in [air_contents]:
    for air_content in air_contents:
        
        st.subheader(f"{air_content} (µg / m^3) vs time")
        fig = px.line(x=data["time"],y=data[air_content])
        fig.update_layout(
            xaxis_title = "time (24-hour)",
            yaxis_title = f"{air_content}"
        )
        st.plotly_chart(fig)
        st.markdown("---")

# co,no,no2,o3,so2,pm2_5,pm10,nh3

def air_content_mean(data):
    """
    Takes the mean of the whole day
    """

    co = (data["co"].mean()) / 1000
    no = data["no"].mean()
    no2 = data["no2"].mean()
    o3 = data["o3"].mean()
    so2 = data["so2"].mean()
    pm2_5 = data["pm2_5"].mean()
    pm10 = data["pm10"].mean()
    nh3 = data["nh3"].mean()

    return {"pm2_5":pm2_5,"pm10": pm10,"no": no,"no2": no2,"nh3": nh3,"co": co,"so2":so2,"o3": o3}
    
def compare_aqi(predicted_aqi):

    if predicted_aqi <= 50:
        st.success("Air quality is good, People are no longer exposed to health risk")
        st.markdown("---")
    elif predicted_aqi > 50 and predicted_aqi <=100:
        st.success("Air Quality is moderate, Acceptable air quality for healthy adults but still pose threat to sensitive individual")
        st.markdown("---")

    elif predicted_aqi > 100 and predicted_aqi <=200:
        st.warning("Air Quality is Poor, which can have health issues such as difficulty in breathing")
        st.markdown("---")

    elif predicted_aqi >200 and predicted_aqi <=300:
        st.warning("Air Quality is unhealthy, can provoke health difficulties especially to the young kids and elderly people")
        st.markdown("---")
    
    elif predicted_aqi > 300 and predicted_aqi <=400:
        st.error("Air Quality is severe, may lead to chronic health issues")
        st.markdown("---")
    
    elif predicted_aqi >400:
        st.error("AQI is exceeding 400 is highly unacceptable to human - can lead to premature death")
        st.markdown("---")
