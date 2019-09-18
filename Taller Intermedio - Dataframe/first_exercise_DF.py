from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('first_exercise').getOrCreate()

df = spark.read.csv("price_paid_records.csv", header=True)
df = df.select(F.col('`Date of Transfer`'), F.substring_index(F.col('`Date of Transfer`'), "-", 1).alias('year'))
df = df.select('year').groupBy('year').count().alias('counts')

df.show()