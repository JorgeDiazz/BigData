from pyspark import SparkContext
import re

sc = SparkContext("local", "spark_exercise_2")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))

# {city, price}
keywords = lines.filter(lambda word: word[1].isdigit()).map(lambda word: (re.sub(r'[^\w\s]', "", word[6].strip()), float(word[1])))

result = keywords.map(lambda keyword: (keyword[0], (keyword[1], 1))) \
	.reduceByKey(lambda value_pair_1, value_pair_2: (value_pair_1[0] + value_pair_2[0], value_pair_1[1] + value_pair_2[1])) \
	.map(lambda key_value: (key_value[0], key_value[1][0] / key_value[1][1]))

result.coalesce(1).saveAsTextFile("result_spark_exercise_2") 
