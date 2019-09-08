from pyspark import SparkContext
import re

def splitLineByYearMonth(line):
	line = line[2].split('-')
	year = line[0]
	month = line[1]
	return (year, month)


sc = SparkContext("local", "spark_exercise_5")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))

result = lines.filter(lambda line: line[1].isdigit()) \
	.map(lambda line: splitLineByYearMonth(line)) \
	.map(lambda year_month_pair: ((year_month_pair[0], year_month_pair[1]), 1)) \
	.reduceByKey(lambda count1, count2: count1 + count2) \
	.map(lambda element: (element[0][0], (element[0][1], element[1]))) \
	.reduceByKey(lambda month_count1, month_count2: (month_count1[0] if month_count1[1] > month_count2[1] else month_count2[0], max(month_count1[1], month_count2[1]))) \
	.map(lambda element: (element[0], element[1][0]))

result.coalesce(1).saveAsTextFile('result_spark_exercise_5')
