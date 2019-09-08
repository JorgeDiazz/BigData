from pyspark import SparkContext
import re

sc = SparkContext("local", "spark_exercise_6")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))

result = lines.filter(lambda line: line[1].isdigit()) \
	.map(lambda line:  ((re.sub(r'[^\w\s]', "", line[8].strip()) , re.sub(r'[^\w\s]', "", line[6].strip())), 1)) \
	.reduceByKey(lambda city1, city2: city1 + city2) \
 	.map(lambda element: (element[0][0], 1)) \
	.reduceByKey(lambda count1, count2: count1 + count2) \
	.map(lambda element: (element[1], 1)) \
	.reduceByKey(lambda count1, count2: count1 + count2) \
	.map(lambda element: (element[1], element[0]))

result.coalesce(1).saveAsTextFile("result_spark_exercise_6")
