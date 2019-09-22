from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('2nd_exercise').getOrCreate()
df = spark.read.option("inferSchema", "true").csv("yellow_tripdata_2019-06.csv", header=True).cache()

df1 = df.select('payment_type').distinct().count()

print(df1)