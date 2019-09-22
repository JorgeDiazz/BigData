from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('5th_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()

df1 = df.groupBy('PULocationID').count()
df2 = df1.select(F.max('count'))

df2 = df2.join(df1, F.col('count') == F.col('max(count)'))

dff = spark.read.option("inferSchema", "true").csv("taxi*", header=True)

df2 = df2.join(dff, F.col('PULocationID') == F.col('LocationID'))

df2 = df2.select('LocationID', 'Borough')

df2.show()