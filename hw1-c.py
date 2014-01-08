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

print (total_petroleum_stocks.T['United States'].values[3:]/10000 - .12 ) / .07

array = (total_petroleum_stocks.T['United States'].values[3:]/10000 - .12 ) / .07

matrix = array.reshape(6,5)


# QUESTION 3:
# Try to create a Hinton diagram, depicting consumption, positive or negative
# and degrees
# http://matplotlib.org/examples/specialty_plots/hinton_demo.html
# Main issue was just reformatting the dataframe into proper size/value range

def hinton(matrix, max_weight=None, ax=None):
    """Draw Hinton diagram for visualizing a weight matrix."""
    ax = ax if ax is not None else plt.gca()

    if not max_weight:
        max_weight = 2**np.ceil(np.log(np.abs(matrix).max())/np.log(2))

    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    for (x,y),w in np.ndenumerate(matrix):
    	if w < .4:
    		color = 'red'
    	elif w < .7:
    		color = 'orange'
    	elif w < .9:
    		color = 'blue'
    	else:
    		color = 'white'
        size = np.sqrt(np.abs(w))
        rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
                             facecolor=color, edgecolor=color)
        ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()


if __name__ == '__main__':
# #	plt.show()
# 	print np.random.rand(20, 20) - 0.5
	hinton(matrix)
	plt.show()
# # How do you map to a shared row/column, other than the above, which takes too long