import os

import requests


def get_weather() -> None:
    api_key = os.environ.get(
        "WEATHER_API_KEY")
    if not api_key:
        print("Error: API key was not found in environ variables!")
        return
    city = "Paris"
    base_url = "https://api.weatherapi.com/v1/current.json"

    url = f"{base_url}?key={api_key}&q={city}"

    response = requests.get(url)

    if response.status_code == 200:
        try:
            weather_data = response.json()
            current_weather = weather_data.get("current", {})
            if current_weather:
                temperature = current_weather.get("temp_c", "N/A")
                condition = current_weather.get(
                    "condition", {}
                ).get("text", "N/A")
                print(f"The weather in {city}: {temperature}°C, {condition}")
            else:
                print("Can not get weather data.")
        except ValueError:
            print("JSON parsing error. The response is not valid JSON.")
    else:
        print(f"Request error. Status: {response.status_code}")
        print(f"Response: {response.text}")


if __name__ == "__main__":
    get_weather()
