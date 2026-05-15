# Weather ETL Pipeline with Airflow, PySpark, and PostgreSQL

## Project Overview

This project is an automated ETL (Extract, Transform, Load) pipeline using:

- Apache Airflow

- PySpark

- PostgreSQL

- Docker

- OpenWeather API

The pipeline:

1. Extracts weather data from OpenWeather API

2. Transforms the data using PySpark

3. Loads the processed data into PostgreSQL

---

## Project Structure

```bash
weather-etl-project/
│
├── dags/
│   └── weather_etl_dag.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── config.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── .env.example
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Project Execution

1. Clone the repository https://github.com/chantharith-NY/Weather-ETL-Pipeline-with-Airflow-PySpark-and-PostgreSQL.git

2. Run docker-compose.yml file

3. Log into Postgres Database with the Username and Password in docker-compose.yml

4. Log into Airflow Web with the username (admin) and password in the terminal.

5. You'll see a DAG file name weather_etl_dag

6. Click on that dag and click run trigger.

---

## Project Features

- Apache Airflow DAG orchestration

- Weather API extraction

- Multi-city data collection

- PySpark transformation

- PostgreSQL loading

- Docker containerization

- Secure environment variable management

- Automated ETL workflow

---

## Future Improvements

- Power BI dashboard

- Streamlit dashboard

- Historical weather storage

- Kafka streaming

- Machine learning prediction

- Real-time monitoring

- Data warehouse integration
