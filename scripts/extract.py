# import requests
# import pandas as pd
# import dotenv
# import os
# from config import API_KEY

# dotenv.load_dotenv()

# def extract_weather():

#     city = "Phnom Penh"

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#     response = requests.get(url)

#     data = response.json()

#     weather_data = {
#         "city": [city],
#         "temperature": [data["main"]["temp"]],
#         "humidity": [data["main"]["humidity"]],
#         "weather": [data["weather"][0]["description"]]
#     }

#     df = pd.DataFrame(weather_data)

#     df.to_csv("/opt/airflow/data/raw/weather.csv", index=False)

#     print("Extraction complete")

# import requests
# import pandas as pd

# API_KEY = "0606622d1bb44008ce82dfa76d2f4b89"

# def extract_weather():

#     city = ["Phnom Penh", "Siem Reap", "Battambang", "Sihanoukville", "Kampot"]

#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

#     response = requests.get(url)

#     data = response.json()

#     print(data)

#     if "main" not in data:
#         raise Exception(f"API Error: {data}")

#     weather_data = {
#         "city": [city],
#         "temperature": [data["main"]["temp"]],
#         "humidity": [data["main"]["humidity"]],
#         "weather": [data["weather"][0]["description"]]
#     }

#     df = pd.DataFrame(weather_data)

#     df.to_csv(
#         "/opt/airflow/data/raw/weather.csv",
#         index=False
#     )

#     print("Extraction complete")

import requests
import pandas as pd

from config import API_KEY


def extract_weather():

    cities = [
        "Phnom Penh",
        "Siem Reap",
        "Battambang",
        "Sihanoukville",
        "Kampot"
    ]

    weather_list = []

    for city in cities:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},KH&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

        print(data)

        if "main" not in data:
            print(f"Skipping city: {city}")
            continue

        weather_list.append({
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        })

    if not weather_list:
        raise Exception("No weather data collected")

    df = pd.DataFrame(weather_list)

    print(df)

    df.to_csv(
        "/opt/airflow/data/raw/weather.csv",
        index=False
    )

    print("Extraction complete")