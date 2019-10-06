# 1st point

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('activity').config("spark.sql.crossJoin.enabled", "true").getOrCreate()
df_ecopetrol = spark.read.option("inferSchema", "true").csv("EC.csv", header=True).cache()
df_avianca = spark.read.option("inferSchema", "true").csv("AVH.csv", header=True).cache()
df_aval = spark.read.option("inferSchema", "true").csv("AVAL.csv", header=True).cache()