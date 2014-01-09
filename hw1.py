# Resource: http://wiki.scipy.org/Cookbook/Matplotlib

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
# US = df_cic.ix['United States'].astype(float).T
# China = df_cic.ix['China'].astype(float).T

# leg=['China', 'United States']

# US_plot = US.plot(xticks=US.index, title ="Imports/Exports in Thousands Barrels per Day")
# # legend in Pandas
# # https://stackoverflow.com/questions/13886019/reconstruction-figure-legend-in-pandas
# US_plot.legend(leg, loc='best')
# plt.xlabel("Year")
# plt.ylabel('Difference between Imports and Exports (Thousand Barrels/Day)')
# # Setting tick intervals
# # https://stackoverflow.com/questions/10839719/how-to-set-step-on-axis-x-in-my-figure-in-matplotlib-python-2-6-6

# China_plot = China.plot(xticks=China.index, title ="Imports/Exports in Thousands Barrels per Day")
# China_plot.legend(leg, loc='best')

# with pd.plot_params.use('x_compat', True):
# 	China.plot(xticks=China.index, title ="Imports/Exports in China")
# 	US.plot(xticks=US.index, title ="Imports/Exports in US")

# plt.show

# QUESTION 2: Bar graph of relative levels of consumption per emission 
# # Measures efficiency of use
# comp = pd.concat([total_consumption, co2_emissions])

# # Uses nested dict comprehension to create map of ratios for the years --> countries

# country_effic_comp = {year: {country: comp[year][country][0]/comp[year][country][1] for country in comp[year].keys() if isinstance(comp[year][country][0], float) and isinstance(comp[year][country][1], float)} for year in comp}

# Creates dataframe from nested dic
# https://stackoverflow.com/questions/13575090/construct-pandas-dataframe-from-items-in-nested-dictionary

# df_cec = pd.DataFrame.from_dict(country_effic_comp)

# US = df_cec.ix['United States'].astype(float).T
# China = df_cec.ix['China'].astype(float).T

# leg = ['China', 'United States']

# US_plot = US.plot()
# # legend in Pandas
# # https://stackoverflow.com/questions/13886019/reconstruction-figure-legend-in-pandas
# US_plot.legend(leg, loc='best')
# plt.xlabel("Year")
# plt.ylabel('Total Consumption/CO2 Emissions')
# # Setting tick intervals
# # https://stackoverflow.com/questions/10839719/how-to-set-step-on-axis-x-in-my-figure-in-matplotlib-python-2-6-6

# China_plot = China.plot(xticks=US.index, title ="Oil consumption as measured in terms of CO2 emissions")
# China_plot.legend(leg, loc='best')

# QUESTION 3:
# Try to create a Hinton diagram, depicting consumption, positive or negative
# and degrees
# http://matplotlib.org/examples/specialty_plots/hinton_demo.html

def hinton(dataframe, max_weight=None, ax=None):
    """Draw Hinton diagram for visualizing a weight matrix."""
    matrix = dataframe.as_matrix()

    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2**np.ceil(np.log(np.abs(matrix).max())/np.log(2))

    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x,y),w in np.ndenumerate(matrix):
        color = 'white' if w > 0 else 'black'
        size = np.sqrt(np.abs(w))
        rect = plt.Rectangle([x - size / 1000, y - size / 1000], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()

hinton(eL.total_supply[1989]['United States'])

if __name__ == '__main__':
	plt.show()
	
# How do you map to a shared row/column, other than the above, which takes too long