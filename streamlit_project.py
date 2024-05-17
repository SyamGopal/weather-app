import streamlit as st
import requests

# HTML template for displaying weather data
weather_template = """
<div class="current-weather">
    <div class="details">
        <h2>{city} ({date})</h2>
        <h6>Temperature: {temp}°C</h6>
        <h6>Wind: {wind} M/S</h6>
        <h6>Humidity: {humidity}%</h6>
    </div>
    <div class="icon">
        <img src="{icon_url}" alt="weather-icon">
        <h6>{description}</h6>
    </div>
</div>
"""

# Streamlit app
def main():
    st.title("Weather Dashboard")
    
    # City input
    city_name = st.text_input("Enter a City Name", "New York")
    
    # Search button
    if st.button("Search", key="search_button"):
        get_city_weather(city_name)
    

# Function to get weather details by city name
def get_city_weather(city_name):
    API_KEY = "0df9f192fff60bad00bf9aad63b5179e"
    WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}"
    
    try:
        response = requests.get(WEATHER_API_URL)
        data = response.json()
        if 'list' in data:
            weather_data = data['list'][0]
            display_weather(weather_data, city_name)
        else:
            st.error("City not found. Please enter a valid city name.")
    except requests.exceptions.RequestException as e:
        st.error("An error occurred while fetching the weather forecast.")
        st.error(str(e))

# Function to display weather data
def display_weather(weather_data, city_name):
    temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    wind_speed = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@4x.png"
    date = weather_data['dt_txt'].split(" ")[0]

    # Display weather template with dynamic data
    st.markdown(weather_template.format(
        city=city_name,
        date=date,
        temp=round(temperature, 2),
        wind=wind_speed,
        humidity=humidity,
        description=description,
        icon_url=icon_url
    ), unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Inline CSS styles
st.markdown("""
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

.container {
    max-width: 800px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.title {
    text-align: center;
    margin-bottom: 20px;
}

.weather-input {
    text-align: center;
    margin-bottom: 20px;
}

.city-input {
    padding: 8px;
    width: 60%;
    margin-right: 10px;
}

.search-btn, .location-btn {
    padding: 8px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.search-btn:hover, .location-btn:hover {
    background-color: #0056b3;
}

.weather-data {
    margin-top: 20px;
}

.current-weather, .days-forecast {
    margin-bottom: 20px;
    border-radius: 8px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
    padding: 20px;
}

.details h2 {
    margin-bottom: 10px;
}

.icon img {
    width: 80px;
    height: 80px;
    display: block;
    margin: 0 auto;
}

.separator {
    margin: 20px 0;
    border-bottom: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)
