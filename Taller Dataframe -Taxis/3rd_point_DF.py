from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('3rd_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()

df1 = df.select('VendorID').groupBy('VendorID').count()

df2 = df1.select(F.max('count'))

df2 = df2.join(df1, F.col('count') == F.col('max(count)')).select('VendorID')

df2.show()
