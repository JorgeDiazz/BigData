from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('5th_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()
dff = spark.read.option("inferSchema", "true").csv("taxi*", header=True)

df1 = dff.where('Zone like "JFK Airport"')

df1 = df1.join(df, F.col('PULocationID') == F.col('LocationID')).alias('first_result')

df2 = dff.where('Zone like "Manhattan Valley"')

df2 = df2.join(df, F.col('DOLocationID') == F.col('LocationID')).alias('second_result')


df3 = df1.join(df2, F.col('first_result.PULocationID') == F.col('second_result.PULocationID'))

df3 = df3.select(F.avg('second_result.trip_distance'), F.avg('second_result.total_amount'))

df3.show()