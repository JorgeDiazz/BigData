from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('5th_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()
dff = spark.read.option("inferSchema", "true").csv("taxi*", header=True)

df1 = df.groupBy('PULocationID', 'DOLocationID').count()
df2 = df1.select(F.max('count'))

df2 = df2.join(df1, F.col('max(count)') == F.col('count'))

df2 = df2.select('PULocationID', 'DOLocationID')

dff1 = dff.select('LocationID', F.col('Zone').alias('PULocationZone'))
dff2 = dff.select('LocationID', F.col('Zone').alias('DOLocationZone'))

df3 = dff1.join(df2, dff1.LocationID == F.col('PULocationID'))
df3 = dff2.join(df3, dff2.LocationID == F.col('DOLocationID'))

df3 = df3.select(F.col('PULocationZone'), F.col('DOLocationZone'))

df3.show()