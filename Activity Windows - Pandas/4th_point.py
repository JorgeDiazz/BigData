# 4th point

# Ecopetrol
max_return_ecopetrol = result.select(F.max('Ecopetrol')) \
    .join(result, result.Ecopetrol == F.col('max(Ecopetrol)')) \
    .select('Year', 'Month', F.lit('Ecopetrol').alias('Company'))

# Avianca
max_return_avianca = result.select(F.max('Avianca')) \
    .join(result, result.Avianca == F.col('max(Avianca)')) \
    .select('Year', 'Month', F.lit('Avianca').alias('Company'))

# Aval
max_return_aval = result.select(F.max('Aval')) \
    .join(result, result.Aval == F.col('max(Aval)')) \
    .select('Year', 'Month', F.lit('Aval').alias('Company'))


result_max_returns = max_return_ecopetrol.union(max_return_avianca).union(max_return_aval)

result_max_returns.show()