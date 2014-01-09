
import excelLoad as eL

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# QUESTION 1: How do China and the U.S. compare in terms of energy independence?
# comp = pd.merge(total_imports, total_exports, right_index=True, left_index=True)
comp = pd.concat([eL.total_imports, eL.total_exports])

country_import_comp = {year: {country: comp[year][country][0] - comp[year][country][1] for country in comp[year].keys() if isinstance(comp[year][country][0], float) and isinstance(comp[year][country][1], float)} for year in comp}

df_cic = pd.DataFrame.from_dict(country_import_comp)

# Note use of ix function to select index
# Need to call astype to convert string numbers to floats for later graphing
# https://stackoverflow.com/questions/16301546/swapping-axes-in-pandas
# Flips axes to make it more readable
US = df_cic.ix['United States'].astype(float).T
China = df_cic.ix['China'].astype(float).T

leg=['China', 'United States']

US_plot = US.plot(xticks=US.index, title ="Imports/Exports in Thousands Barrels per Day")
# # legend in Pandas
# # https://stackoverflow.com/questions/13886019/reconstruction-figure-legend-in-pandas
US_plot.legend(leg, loc='best')
plt.xlabel("Year")
plt.ylabel('Difference between Imports and Exports (Thousand Barrels/Day)')
# # Setting tick intervals
# # https://stackoverflow.com/questions/10839719/how-to-set-step-on-axis-x-in-my-figure-in-matplotlib-python-2-6-6

China_plot = China.plot(xticks=China.index, title ="Imports/Exports in Thousands Barrels per Day")
China_plot.legend(leg, loc='best')

# with pd.plot_params.use('x_compat', True):
# 	China.plot(xticks=China.index, title ="Imports/Exports in China")
# 	US.plot(xticks=US.index, title ="Imports/Exports in US")

plt.show()
