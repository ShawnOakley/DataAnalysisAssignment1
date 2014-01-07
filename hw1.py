import pandas as pd


def key_float_to_string(df):
	df.keys = [int(key) for key in df.keys() ]
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

comp = pd.merge(total_imports, total_exports)
print total_exports.keys

