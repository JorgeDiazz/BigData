from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('second_exercise').getOrCreate()
df = spark.read.csv("price_paid_records.csv", header=True)
df = df.withColumn('Price', df.Price.cast('double'))
df = df.groupBy('Town/City').avg('Price')

df.show()
