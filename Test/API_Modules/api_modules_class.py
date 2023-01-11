import requests


# This class is responsible to all possible API requests we might require
class APIModulesClass:
    def __init__(self):
        self.appid= "439d4b804bc8187953eb36d2a8c26a02"
    # This class uses given "appid", longitude and latitude of the required location
    # in order to retrieve the data of the current weather within the provided location
    # It is returned as JSON file for further tests
    def retrieve_api_weather_data(self, city_data):
        request_url = \
            f'https://openweathermap.org/data/2.5/onecall?lat={city_data["latitude"]}&lon={city_data["longitude"]}&' \
            f'units=metric&appid={self.appid}'

        return requests.post(request_url, json={}, headers={'Content-Type': 'application/json'}).json()["current"]