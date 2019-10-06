# 8th, 10th & 11th point

# Ecopetrol

fig, ax = plt.subplots()

ax.plot(upper_band_ecopetrol_pd.Date, upper_band_ecopetrol_pd.upper_band, label='Upper band')
ax.plot(ecopetrol_pd.Date, ecopetrol_pd.Close, label='Original values')
ax.plot(lower_band_ecopetrol_pd.Date, lower_band_ecopetrol_pd.lower_band, label='Lower band')

ax.legend(loc='upper right')
ax.set_title('Ecopetrol')

# comparing with upper band
df_upper_band_ecopetrol = df_upper_band_ecopetrol.select(F.col('Date').alias('DateUpperBand'), 'upper_band')

df_upper_offset_ecopetrol = df1_ecopetrol.join(df_upper_band_ecopetrol, (df1_ecopetrol.Close > df_upper_band_ecopetrol.upper_band) & (df1_ecopetrol.Date == df_upper_band_ecopetrol.DateUpperBand))

df_upper_offset_ecopetrol = df_upper_offset_ecopetrol.select('Date', F.lit('Sell').alias('Action'))

# comparing with lower band
df_lower_band_ecopetrol = df_lower_band_ecopetrol.select(F.col('Date').alias('DateLowerBand'), 'lower_band')

df_lower_offset_ecopetrol = df1_ecopetrol.join(df_lower_band_ecopetrol, (df1_ecopetrol.Close < df_lower_band_ecopetrol.lower_band) & (df1_ecopetrol.Date == df_lower_band_ecopetrol.DateLowerBand))
df_lower_offset_ecopetrol = df_lower_offset_ecopetrol.select('Date', F.lit('Buy').alias('Action'))

result_ecopetrol = df_upper_offset_ecopetrol.union(df_lower_offset_ecopetrol).distinct() \
    .select(F.to_date('Date').alias('Date'), 'Action').orderBy('Date')

print('Ecopetrol:')
result_ecopetrol.show()


# Avianca

fig, ax = plt.subplots()

ax.plot(upper_band_avianca_pd.Date, upper_band_avianca_pd.upper_band, label='Upper band')
ax.plot(avianca_pd.Date, avianca_pd.Close, label='Original values')
ax.plot(lower_band_avianca_pd.Date, lower_band_avianca_pd.lower_band, label='Lower band')

ax.legend(loc='upper right')
ax.set_title('Avianca')

# comparing with upper band
df_upper_band_avianca = df_upper_band_avianca.select(F.col('Date').alias('DateUpperBand'), 'upper_band')

df_upper_offset_avianca = df1_avianca.join(df_upper_band_avianca, (df1_avianca.Close > df_upper_band_avianca.upper_band) & (df1_avianca.Date == df_upper_band_avianca.DateUpperBand))

df_upper_offset_avianca = df_upper_offset_avianca.select('Date', F.lit('Sell').alias('Action'))

# comparing with lower band
df_lower_band_avianca = df_lower_band_avianca.select(F.col('Date').alias('DateLowerBand'), 'lower_band')

df_lower_offset_avianca = df1_avianca.join(df_lower_band_avianca, (df1_avianca.Close < df_lower_band_avianca.lower_band) & (df1_avianca.Date == df_lower_band_avianca.DateLowerBand))
df_lower_offset_avianca = df_lower_offset_avianca.select('Date', F.lit('Buy').alias('Action'))

result_avianca = df_upper_offset_avianca.union(df_lower_offset_avianca).distinct() \
    .select(F.to_date('Date').alias('Date'), 'Action').orderBy('Date')

print('Avianca:')
result_avianca.show()


# Aval

fig, ax = plt.subplots()

ax.plot(upper_band_aval_pd.Date, upper_band_aval_pd.upper_band, label='Upper band')
ax.plot(aval_pd.Date, aval_pd.Close, label='Original values')
ax.plot(lower_band_aval_pd.Date, lower_band_aval_pd.lower_band, label='Lower band')

ax.legend(loc='lower right')
ax.set_title('Aval')

# comparing with upper band
df_upper_band_aval = df_upper_band_aval.select(F.col('Date').alias('DateUpperBand'), 'upper_band')

df_upper_offset_aval = df1_aval.join(df_upper_band_aval, (df1_aval.Close > df_upper_band_aval.upper_band) & (df1_aval.Date == df_upper_band_aval.DateUpperBand))

df_upper_offset_aval = df_upper_offset_aval.select('Date', F.lit('Sell').alias('Action'))

# comparing with lower band
df_lower_band_aval = df_lower_band_aval.select(F.col('Date').alias('DateLowerBand'), 'lower_band')

df_lower_offset_aval = df1_aval.join(df_lower_band_aval, (df1_aval.Close < df_lower_band_aval.lower_band) & (df1_aval.Date == df_lower_band_aval.DateLowerBand))
df_lower_offset_aval = df_lower_offset_aval.select('Date', F.lit('Buy').alias('Action'))

result_aval = df_upper_offset_aval.union(df_lower_offset_aval).distinct() \
    .select(F.to_date('Date').alias('Date'), 'Action').orderBy('Date')

print('Aval:')
result_aval.show()