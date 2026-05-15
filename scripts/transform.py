from pyspark.sql import SparkSession

def transform_weather():

    spark = SparkSession.builder \
        .appName("WeatherTransform") \
        .getOrCreate()

    df = spark.read.csv(
        "/opt/airflow/data/raw/weather.csv",
        header=True,
        inferSchema=True
    )

    df = df.dropna()

    df.show()

    df.write.mode("overwrite").csv(
        "/opt/airflow/data/processed/weather_clean.csv",
        header=True
    )

    spark.stop()

    print("Transformation complete")