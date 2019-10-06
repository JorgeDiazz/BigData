# 5th point 

from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

twentyDaysBefore = -20

window = Window.rowsBetween(twentyDaysBefore, 0)
df1_ecopetrol = df_ecopetrol.select('Date', F.avg('Close').over(window).alias('moving_avg'))

# plotting

fig, ax = plt.subplots()

ecopetrol_pd = df1_ecopetrol.toPandas()

ecopetrol_pd.set_index('Date')

ax.plot(ecopetrol_pd.Date, ecopetrol_pd.moving_avg, label='Ecopetrol')

ax.legend(loc='upper right')