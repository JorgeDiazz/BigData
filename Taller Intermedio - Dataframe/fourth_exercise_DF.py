from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('fourth_exercise').getOrCreate()
df = spark.read.csv("price_paid_records.csv", header=True)

df = df.withColumn('Price', df.Price.cast('double'))
df = df.where("`Town/City` like '%STAMFORD%' and `Date of Transfer` like '2015%'")
df = df.select('Price').orderBy('Price')

df.show()