from pyspark import SparkContext
import re

sc = SparkContext("local", "spark_exercise_3")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))

# {city, price}
keywords = lines.filter(lambda word: word[1].isdigit()).map(lambda word: (re.sub(r'[^\w\s]', "", word[6].strip()), float(word[1])))

result = keywords.reduceByKey(lambda value1, value2: min(value1, value2))

result.coalesce(1).saveAsTextFile("result_spark_exercise_3") 
