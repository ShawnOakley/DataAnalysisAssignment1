import pandas as pd
import matplotlib.pyplot as plt


def key_float_to_string(df):
	df.keys = [int(key) for key in df.keys() ]
	df.columns = [int(key) for key in df.columns ]
	return df

def to_number(s):
 	try:
 		s1 = float(s)
 		return s1
 	except ValueError:
 		return 0

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

# Note use of ix function to select index
# Need to call astype to convert string numbers to floats for later graphing
US = comp.ix['United States'].astype(float).T
China = comp.ix['China'].astype(float).T
# print comp.keys
# print comp.applymap(lambda x: x[0]-x[1])
# print comp.values['Mexico']
# print total_exports.index
# print total_exports.columns
# print total_exports.keys

# https://stackoverflow.com/questions/16301546/swapping-axes-in-pandas
# Flips axes to make it more readable


US.plot()

# Setting tick intervals
# https://stackoverflow.com/questions/10839719/how-to-set-step-on-axis-x-in-my-figure-in-matplotlib-python-2-6-6
plt.xticks(US.index)


China.plot()
plt.xticks(China.index)

plt.show()