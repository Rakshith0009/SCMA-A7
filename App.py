import streamlit as st
import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Streamlit app
def main():
    st.title("Weather Forecasting App")

    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

    city = st.text_input("Enter a city name:")
    
    if city:
        weather_data = get_weather(city, api_key)
        
        if weather_data.get("cod") != 200:
            st.error("City not found. Please enter a valid city name.")
        else:
            st.subheader(f"Weather in {city.capitalize()}:")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    
if __name__ == "__main__":
    main()
