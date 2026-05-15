# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# from scripts.extract import extract_weather
# from scripts.transform import transform_weather
# from scripts.load import load_weather

# with DAG(
#     dag_id="weather_etl_pipeline",
#     start_date=datetime(2025, 1, 1),
#     schedule="@daily",
#     catchup=False
# ) as dag:

#     extract_task = PythonOperator(
#         task_id="extract_weather",
#         python_callable=extract_weather
#     )

#     transform_task = PythonOperator(
#         task_id="transform_weather",
#         python_callable=transform_weather
#     )

#     load_task = PythonOperator(
#         task_id="load_weather",
#         python_callable=load_weather
#     )

#     extract_task >> transform_task >> load_task

# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime

# import sys
# sys.path.append('/opt/airflow/scripts')

# from scripts.extract import extract_weather
# from scripts.transform import transform_weather
# from scripts.load import load_weather

# with DAG(
#     dag_id="weather_etl_pipeline",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="@daily",
#     catchup=False
# ) as dag:

#     extract_task = PythonOperator(
#         task_id="extract_weather",
#         python_callable=extract_weather
#     )

#     transform_task = PythonOperator(
#         task_id="transform_weather",
#         python_callable=transform_weather
#     )

#     load_task = PythonOperator(
#         task_id="load_weather",
#         python_callable=load_weather
#     )


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

import sys
sys.path.append('/opt/airflow/scripts')

from extract import extract_weather
from transform import transform_weather
from load import load_weather

with DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract_weather",
        python_callable=extract_weather
    )

    transform_task = PythonOperator(
        task_id="transform_weather",
        python_callable=transform_weather
    )

    load_task = PythonOperator(
        task_id="load_weather",
        python_callable=load_weather
    )

    extract_task >> transform_task >> load_task