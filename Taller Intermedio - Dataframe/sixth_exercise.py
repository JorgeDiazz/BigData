from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('sixth_exercise').getOrCreate()
df = spark.read.csv("price_paid_records.csv", header=True)

df = df.select("`Town/City`", "County").distinct().groupBy("County").count().alias("CitiesCount").select(F.col("CitiesCount.count").alias("cities_number"))
df = df.groupBy("cities_number").count().alias("CountiesCount")
df = df.select(F.col("CountiesCount.count").alias("num_counties"),F.col("cities_number").alias("num_cities")) 