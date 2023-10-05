from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load env file so we can access api key
load_dotenv()


def getCurrentWeather(city="Timbuktu"):

    try:

        request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

        weather_data = requests.get(request_url).json()

        return weather_data

    except:
        print("An error has occurred")


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')
    city = input('\nPlease enter a city name: ')

    # when running from command line, if city is blank, empty or just spaces, after stripping
    # white space, we set a default value of 'timbuktu'
    if not bool(city.strip()):
        city = "Timbuktu"

    weather_data = getCurrentWeather(city)
    print('\n')
    pprint(weather_data)
