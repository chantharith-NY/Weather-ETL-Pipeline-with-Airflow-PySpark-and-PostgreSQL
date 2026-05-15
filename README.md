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
