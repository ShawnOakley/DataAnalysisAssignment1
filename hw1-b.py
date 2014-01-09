
import excelLoad as eL

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# QUESTION 2: Bar graph of relative levels of consumption per emission 
# Measures efficiency of use
comp = pd.concat([eL.total_consumption, eL.co2_emissions])

# # Uses nested dict comprehension to create map of ratios for the years --> countries

country_effic_comp = {year: {country: comp[year][country][0]/comp[year][country][1] for country in comp[year].keys() if isinstance(comp[year][country][0], float) and isinstance(comp[year][country][1], float)} for year in comp}

# Creates dataframe from nested dic
# https://stackoverflow.com/questions/13575090/construct-pandas-dataframe-from-items-in-nested-dictionary

df_cec = pd.DataFrame.from_dict(country_effic_comp)

US = df_cec.ix['United States'].astype(float).T
China = df_cec.ix['China'].astype(float).T

leg = ['China', 'United States']

US_plot = US.plot()
# # legend in Pandas
# # https://stackoverflow.com/questions/13886019/reconstruction-figure-legend-in-pandas
US_plot.legend(leg, loc='best')
plt.xlabel("Year")
plt.ylabel('Total Consumption/CO2 Emissions')
# Setting tick intervals
# https://stackoverflow.com/questions/10839719/how-to-set-step-on-axis-x-in-my-figure-in-matplotlib-python-2-6-6

China_plot = China.plot(xticks=US.index[0::5], title ="Oil consumption as measured in terms of CO2 emissions")
China_plot.legend(leg, loc='best')

plt.show()