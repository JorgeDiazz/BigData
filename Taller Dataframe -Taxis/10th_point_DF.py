from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('5th_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()

df1 = df.select(F.avg(df.tpep_dropoff_datetime.cast('long') - df.tpep_pickup_datetime.cast('long')).alias('trip_time_average'))

df1.show()