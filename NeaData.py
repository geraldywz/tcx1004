import requests
from enum import Enum

NEA_DATA_END_POINT = "https://api.data.gov.sg/v1/environment/{}"

class NeaDataApi(Enum):
    TWO_HOUR_FORECAST = NEA_DATA_END_POINT.format("2-hour-weather-forecast")
    TWENTY_FOUR_HOUR_FORECAST = NEA_DATA_END_POINT.format("24-hour-weather-forecast")
    FOUR_DAY_FORECAST = NEA_DATA_END_POINT.format("4-day-weather-forecast")

def get_weather_data(api: NeaDataApi):
    try:
        response = requests.get(api.value)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch data for {api.name}\n({api.value}). "
                                  f"\nStatus code: {response.status_code}\nResponse: {response.text}")
        return response.json()
    except requests.RequestException as e:
        raise ConnectionError(f"Error while connecting to {api.name} ({api.value}): {str(e)}")

def get_2h_forecast():
    data = get_weather_data(NeaDataApi.TWO_HOUR_FORECAST)
    return data['items'][0]['forecasts']

def get_24h_forecast():
    data = get_weather_data(NeaDataApi.TWENTY_FOUR_HOUR_FORECAST)
    return data['items'][0]['forecasts']

def get_4d_forecast():
    data = get_weather_data(NeaDataApi.FOUR_DAY_FORECAST)
    return data['items'][0]['forecasts']