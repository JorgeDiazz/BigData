# 7th point

twentyDaysBefore = -20

window = Window.rowsBetween(twentyDaysBefore, 0)

k = 2
upper_band = F.col('moving_avg') + (k * F.col('std_deviation')) 
lower_band = F.col('moving_avg') - (k * F.col('std_deviation'))

# Ecopetrol

df1_ecopetrol = df_ecopetrol.select('Date', 'Close', F.avg('Close').over(window).alias('moving_avg'), \
                                    F.stddev('Close').over(window).alias('std_deviation'))

df_upper_band_ecopetrol = df1_ecopetrol.select('Date', upper_band.alias('upper_band'))
df_lower_band_ecopetrol = df1_ecopetrol.select('Date', lower_band.alias('lower_band'))

# plotting

fig, ax = plt.subplots()

moving_avg_ecopetrol_pd = df1_ecopetrol.toPandas()
upper_band_ecopetrol_pd = df_upper_band_ecopetrol.toPandas()
lower_band_ecopetrol_pd = df_lower_band_ecopetrol.toPandas()

moving_avg_ecopetrol_pd.set_index('Date')
upper_band_ecopetrol_pd.set_index('Date')
lower_band_ecopetrol_pd.set_index('Date')

ax.plot(upper_band_ecopetrol_pd.Date, upper_band_ecopetrol_pd.upper_band, label='Upper band')
ax.plot(moving_avg_ecopetrol_pd.Date, moving_avg_ecopetrol_pd.moving_avg, label='Middle band')
ax.plot(lower_band_ecopetrol_pd.Date, lower_band_ecopetrol_pd.lower_band, label='Lower band')

ax.legend(loc='upper right')
ax.set_title('Ecopetrol')


# Avianca

df1_avianca = df_avianca.select('Date', 'Close', F.avg('Close').over(window).alias('moving_avg'), \
                                    F.stddev('Close').over(window).alias('std_deviation'))

df_upper_band_avianca = df1_avianca.select('Date', upper_band.alias('upper_band'))
df_lower_band_avianca = df1_avianca.select('Date', lower_band.alias('lower_band'))

# plotting

fig, ax = plt.subplots()

moving_avg_avianca_pd = df1_avianca.toPandas()
upper_band_avianca_pd = df_upper_band_avianca.toPandas()
lower_band_avianca_pd = df_lower_band_avianca.toPandas()

moving_avg_avianca_pd.set_index('Date')
upper_band_avianca_pd.set_index('Date')
lower_band_avianca_pd.set_index('Date')

ax.plot(upper_band_avianca_pd.Date, upper_band_avianca_pd.upper_band, label='Upper band')
ax.plot(moving_avg_avianca_pd.Date, moving_avg_avianca_pd.moving_avg, label='Middle band')
ax.plot(lower_band_avianca_pd.Date, lower_band_avianca_pd.lower_band, label='Lower band')

ax.legend(loc='upper right')
ax.set_title('Avianca')


# Aval

df1_aval = df_aval.select('Date', 'Close', F.avg('Close').over(window).alias('moving_avg'), \
                                    F.stddev('Close').over(window).alias('std_deviation'))

df_upper_band_aval = df1_aval.select('Date', upper_band.alias('upper_band'))
df_lower_band_aval = df1_aval.select('Date', lower_band.alias('lower_band'))

# plotting

fig, ax = plt.subplots()

moving_avg_aval_pd = df1_aval.toPandas()
upper_band_aval_pd = df_upper_band_aval.toPandas()
lower_band_aval_pd = df_lower_band_aval.toPandas()

moving_avg_aval_pd.set_index('Date')
upper_band_aval_pd.set_index('Date')
lower_band_aval_pd.set_index('Date')

ax.plot(upper_band_aval_pd.Date, upper_band_aval_pd.upper_band, label='Upper band')
ax.plot(moving_avg_aval_pd.Date, moving_avg_aval_pd.moving_avg, label='Middle band')
ax.plot(lower_band_aval_pd.Date, lower_band_aval_pd.lower_band, label='Lower band')

ax.legend(loc='upper right')
ax.set_title('Aval')