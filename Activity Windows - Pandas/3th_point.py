# 3th point

from pyspark.sql import Window

monthWindow = Window.partitionBy('Year', 'Month') \
    .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)

get_first_open = F.lit(F.first('Open')).over(monthWindow).alias('first_open')
get_first_close = F.lit(F.first('Close')).over(monthWindow).alias('first_close')
get_last_open = F.lit(F.last('Open')).over(monthWindow).alias('last_open')
get_last_close = F.lit(F.last('Close')).over(monthWindow).alias('last_close')

monthly_return_operation = 100 * (((F.col('first_open') - F.col('first_close')) / F.col('first_open')) \
                                  + ((F.col('last_open') - F.col('last_close')) / F.col('last_open'))) / 2

# Ecopetrol
df1_ecopetrol = df_ecopetrol.select(F.year('Date').alias('Year'), F.month('Date').alias('Month'), 'Open', 'Close')

df1_ecopetrol = df1_ecopetrol.select('Year', 'Month', \
                                     get_first_open, \
                                     get_first_close, \
                                     get_last_open, \
                                     get_last_close) \
                                    .distinct() \
                                    .orderBy('Year', 'Month')

df1_ecopetrol = df1_ecopetrol.select('Year', 'Month', monthly_return_operation.alias('Ecopetrol'))

# Avianca
df1_avianca = df_avianca.select(F.year('Date').alias('Year'), F.month('Date').alias('Month'), 'Open', 'Close')

df1_avianca = df1_avianca.select('Year', 'Month', \
                                     get_first_open, \
                                     get_first_close, \
                                     get_last_open, \
                                     get_last_close) \
                                    .distinct() \
                                    .orderBy('Year', 'Month')

df1_avianca = df1_avianca.select(F.col('Year').alias('Year1'), F.col('Month').alias('Month1'), monthly_return_operation.alias('Avianca'))

# Aval
df1_aval = df_aval.select(F.year('Date').alias('Year'), F.month('Date').alias('Month'), 'Open', 'Close')

df1_aval = df1_aval.select('Year', 'Month', \
                                     get_first_open, \
                                     get_first_close, \
                                     get_last_open, \
                                     get_last_close) \
                                    .distinct() \
                                    .orderBy('Year', 'Month')

df1_aval = df1_aval.select(F.col('Year').alias('Year2'), F.col('Month').alias('Month2'), monthly_return_operation.alias('Aval'))


result = df1_ecopetrol.join(df1_avianca, (F.col('Year') == F.col('Year1')) & (F.col('Month') == F.col('Month1'))) \
    .join(df1_aval, (F.col('Year') == F.col('Year2')) & (F.col('Month') == F.col('Month2'))) \
    .select('Year', 'Month', 'Ecopetrol', 'Avianca', 'Aval') \
    .filter('Month != 9')

result.show()