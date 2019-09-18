from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('fifth_exercise').getOrCreate()

df = spark.read.csv("price_paid_records.csv", header=True)
df = df.select(F.col('`Date of Transfer`'), F.substring_index(F.col('`Date of Transfer`'), "-", 1).alias('year'))
df = df.select('year', F.split('`Date of Transfer`', "-")[1].alias('month'))
df = df.withColumn('month', df.month.cast('integer'))


df1 = df.groupBy('year', 'month').count().groupBy('year').max('count').alias('counts')
df = df.groupBy('year', 'month').count().alias('original')

df = df.join(df1, (F.col('original.count') == F.col('counts.max(count)')) & (F.col('original.year') == F.col('counts.year')))
df = df.select('original.year', 'original.month') 

df.show()
