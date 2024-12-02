#Location: C:\Users\amna_\OneDrive\Dokumente\Codes,program\Python files

import streamlit as st
import requests

def get_weather(): 
# Define the Open-Meteo API endpoint for current weather
 url = "https://api.open-meteo.com/v1/forecast"

# Define the parameters for the API request (latitude and longitude for Berlin)
 params = {
     "latitude": 52.52,  # Latitude for Berlin
     "longitude": 13.405,  # Longitude for Berlin
     "current_weather": "true",  # Request current weather data
     "timezone": get_input1  # Timezone for the data
 }


 response = requests.get(url, params=params)

# Check if the request was successful
 if response.status_code == 200:
     # Parse the JSON response
     data = response.json()
 
     # Extract the relevant data
     temperature = data["current_weather"]["temperature"]
     windspeed = data["current_weather"]["windspeed"]
     weather_code = data["current_weather"]["weathercode"]

     # Map weather codes to weather icons (simplified)
     weather_icons = {
         0: "Clear sky",       # Clear sky (sunny)
         1: "Mainly clear",    # Mostly clear
         2: "Partly cloudy",   # Partly cloudy
         3: "Cloudy",          # Cloudy 
         45: "Fog",            # Fog
         51: "Drizzle",        # Drizzle
         61: "Rain",           # Rain
         71: "Snow",           # Snow
     }
    
    # Get the weather description based on the weather code
     weather_description = weather_icons.get(weather_code, "Unknown weather")
    
    # Display the extracted data
     st.title(f"Temperature: {temperature}°C")
     st.title(f"Windspeed: {windspeed} km/h")
     st.title(f"Weather: {weather_description}")
    
    # You can also map the weather code to an icon
     if weather_code == 0:
         st.title("Icon: 🌞 (Sunny)")
     elif weather_code == 1 or weather_code == 2:
         st.title("Icon: 🌤 (Partly Cloudy)")
     elif weather_code == 3:
         st.title("Icon: ☁️ (Cloudy)")
     elif weather_code == 45:
         st.title("Icon: 🌫 (Foggy)")
     elif weather_code == 51 or weather_code == 61:
         st.title("Icon: 🌧 (Rainy)")
     elif weather_code == 71:
         st.title("Icon: ❄️ (Snowy)")
     else:
         st.title("Icon: ❓ (Unknown Weather)")
 else:
     st.title(" ")


st.set_page_config(page_title="KrankiRain.ai", page_icon="🌍", layout="centered")

st.title("Welcome to KrankiRain.ai 👋🏻")
st.caption("Stay ahead with KrankiRain.ai! Get real-time forecasts, detailed weather updates, and personalized alerts to plan your day confidently, wherever you are. ⚡")
st.divider()

get_input1 = get_vid = st.text_input("Enter your city (ONLY EUROPE) 🔗")

button1 = st.button("✨ Get Weather")

button1 = get_weather()