# 2nd point

daily_return_operation = 100 * (F.col('Open') - F.col('Close')) / F.col('Open')

# Ecopetrol
df1_ecopetrol = df_ecopetrol.select('Date', daily_return_operation.alias('Ecopetrol'))

# Avianca
df1_avianca = df_avianca.select(F.col('Date').alias('Date1'), daily_return_operation.alias('Avianca'))

# Aval
df1_aval = df_aval.select(F.col('Date').alias('Date2'), daily_return_operation.alias('Aval'))

result = df1_ecopetrol.join(df1_avianca, F.col('Date') == F.col('Date1')) \
    .join(df1_aval, F.col('Date1') == F.col('Date2')) \
    .select(F.to_date('Date').alias('Date'), 'Ecopetrol', 'Avianca', 'Aval')

result.show()