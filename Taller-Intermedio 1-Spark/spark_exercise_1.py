from pyspark import SparkContext

sc = SparkContext("local", "spark_exercise_1")
rdd = sc.textFile("price_paid_records.csv")

lines = rdd.map(lambda words: words.split(','))
keywords = lines.map(lambda word: str(word[2])[0:str(word[2]).find('-')])
years = keywords.filter(lambda word: word.isdigit())

keywords = years.map(lambda year: (year, 1))

result = keywords.reduceByKey(lambda key1, key2: key1 + key2)

result.saveAsTextFile("result_spark_exercise_1")
