# import pandas as pd
# from sqlalchemy import create_engine

# def load_weather():

#     df = pd.read_csv(
#         "/opt/airflow/data/processed/weather_clean.csv/part-00000*.csv"
#     )

#     engine = create_engine(
#         "postgresql://airflow:airflow@postgres/weatherdb"
#     )

#     df.to_sql(
#         "weather_data",
#         engine,
#         if_exists="replace",
#         index=False
#     )

#     print("Load complete")

import pandas as pd
from sqlalchemy import create_engine
import glob

from config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB

def load_weather():

    files = glob.glob(
        "/opt/airflow/data/processed/weather_clean.csv/part-*.csv"
    )

    if not files:
        raise Exception("No transformed CSV file found")

    df = pd.read_csv(files[0])

    engine = create_engine(
        # "postgresql://airflow:airflow@postgres/weatherdb"
        "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
    )

    df.to_sql(
        "weather_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Load complete")