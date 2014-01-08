# Resource: http://wiki.scipy.org/Cookbook/Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def key_float_to_string(df):
	df.keys = [int(key) for key in df.keys() ]
	df.columns = [int(key) for key in df.columns ]
	return df

co2_emissions = pd.ExcelFile('CO2_Emissions_from_the_Consumption_of_Petroleum_(Million_Metric_Tons).xls')
co2_emissions = key_float_to_string(co2_emissions.parse('Data3'))

bunkering = pd.ExcelFile('Consumption_of_Residual_Fuel_Oil_for_Bunkering_(Thousand_Barrels_Per_Day).xls')
bunkering = key_float_to_string(bunkering.parse('Data3'))

distillation_capacity = pd.ExcelFile('Crude_Oil_Distillation_Capacity_(Thousand_Barrels_Per_Cal_Day).xls')
distillation_capacity = key_float_to_string(distillation_capacity.parse('Data3'))

reserves = pd.ExcelFile('Crude_Oil_Proved_Reserves_(Billion_Barrels).xls')
reserves = key_float_to_string(reserves.parse('Data3'))

gross_heat_content = pd.ExcelFile('Gross_Heat_Content_of_Crude_Oil_Production_(Thousand_Btu_per_Barrel).xls')
gross_heat_content = key_float_to_string(gross_heat_content.parse('Data3'))

total_exports = pd.ExcelFile('Total_Exports_of_Refined_Petroleum_Products_(Thousand_Barrels_Per_Day).xls')
total_exports = key_float_to_string(total_exports.parse('Data3'))

total_imports = pd.ExcelFile('Total_Imports_of_Refined_Petroleum_Products_(Thousand_Barrels_Per_Day).xls')
total_imports = key_float_to_string(total_imports.parse('Data3'))

total_supply = pd.ExcelFile('Total_Oil_Supply_(Thousand_Barrels_Per_Day).xls')
total_supply = key_float_to_string(total_supply.parse('Data3'))

total_consumption = pd.ExcelFile('Total_Petroleum_Consumption_(Thousand_Barrels_Per_Day).xls')
total_consumption = key_float_to_string(total_consumption.parse('Data3'))

total_petroleum_stocks = pd.ExcelFile('Total_Petroleum_Stocks,_End_of_Period_(Millions_Barrels).xls')
total_petroleum_stocks = key_float_to_string(total_petroleum_stocks.parse('Data3'))


# QUESTION 1: How do China and the U.S. compare in terms of energy independence?
# comp = pd.merge(total_imports, total_exports, right_index=True, left_index=True)
comp = pd.concat([total_imports, total_exports])

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

hinton(total_supply[1989]['United States'])

if __name__ == '__main__':
	plt.show()
	
# How do you map to a shared row/column, other than the above, which takes too long