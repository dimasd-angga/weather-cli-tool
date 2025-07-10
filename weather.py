import requests
import argparse
import os

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Celsius
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            print(f"Error: {data['message']}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Get current weather for a city.')
    parser.add_argument('city', type=str, help='City name')
    args = parser.parse_args()
    
    api_key = os.getenv('OWM_API_KEY')  # Get API key from environment variable
    
    if not api_key:
        print("ERROR: Environment variable 'OWM_API_KEY' not set.")
        print("Get a free API key: https://openweathermap.org/api")
        return
    
    weather = get_weather(api_key, args.city)
    
    if weather:
        print(f"\nWeather in {weather['city']}:")
        print(f"• Temperature: {weather['temp']}°C")
        print(f"• Conditions: {weather['description'].capitalize()}")
        print(f"• Humidity: {weather['humidity']}%")
        print(f"• Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    main()
