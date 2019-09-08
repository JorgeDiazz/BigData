from pyspark import SparkContext
import re

sc = SparkContext("local", "spark_exercise_4")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))
# {STAMFORD, 2015 price}
keywords = lines.filter(lambda word: word[1].isdigit() and re.sub(r'[^\w\s]', "", word[6].strip()) == 'STAMFORD' and word[2].strip()[0 : word[2].strip().find('-')].strip() == '2015') \
	.map(lambda word: float(word[1]))               

result = keywords.sortBy(lambda price: price)

result.coalesce(1).saveAsTextFile("result_spark_exercise_4") 
