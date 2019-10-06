# 6th point

fig, ax = plt.subplots()

ecopetrol_pd = df_ecopetrol.toPandas()
avianca_pd = df_avianca.toPandas()
aval_pd = df_aval.toPandas()

ecopetrol_pd.set_index('Date')
avianca_pd.set_index('Date')
aval_pd.set_index('Date')

ax.plot(ecopetrol_pd.Date, ecopetrol_pd.Close, label='Ecopetrol')
ax.plot(avianca_pd.Date, avianca_pd.Close, label='Avianca')
ax.plot(aval_pd.Date, aval_pd.Close, label='Aval')

ax.legend(loc='upper right')