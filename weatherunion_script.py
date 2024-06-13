import requests
from laggeddata import *

API_KEY = "24b3227970223a36294433a167dc358b"
BASE_URL = "https://www.weatherunion.com/gw/weather/external/v0"

def get_locality_weather_data(locality_id):
    url = f"{BASE_URL}/get_locality_weather_data"
    headers = {
        "Content-Type": "application/json",
        "x-zomato-api-key": API_KEY
    }
    params = {
        "locality_id": locality_id
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

kolkata='ZWL005429'
howrah='ZWL002488'
sectorV='ZWL002931'
airport='ZWL005435'
rabindrasadan='ZWL005244'
dakshindari='ZWL001499'

locality_weather_data = get_locality_weather_data(kolkata)

hourly_demand['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']


locality_weather_data= get_locality_weather_data(rabindrasadan)
hourly_demand_rabindrasadan['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_rabindrasadan['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_rabindrasadan['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']

locality_weather_data= get_locality_weather_data(dakshindari)
hourly_demand_dakshinDari['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_dakshinDari['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_dakshinDari['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']

locality_weather_data= get_locality_weather_data(airport)
hourly_demand_airpot['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_airpot['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_airpot['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']

locality_weather_data= get_locality_weather_data(howrah)
hourly_demand_howrah['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_howrah['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_howrah['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']

locality_weather_data= get_locality_weather_data(sectorV)
hourly_demand_sectorV['temperature'] = locality_weather_data['locality_weather_data']['temperature']
hourly_demand_sectorV['rain_intensity'] = locality_weather_data['locality_weather_data']['rain_intensity']
hourly_demand_sectorV['rain_accumulation'] = locality_weather_data['locality_weather_data']['rain_accumulation']


print("WeatherUnion Script fetched")