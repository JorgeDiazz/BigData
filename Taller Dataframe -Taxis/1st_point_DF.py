from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('1st_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()

df1 = df.select(F.avg('trip_distance'))

df1.show()