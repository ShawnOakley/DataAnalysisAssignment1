import pandas as pd

co2_emissions = pd.ExcelFile('CO2_Emissions_from_the_Consumption_of_Petroleum_(Million_Metric_Tons).xls')
co2_emissions = co2_emissions.parse('Data3')

bunkering = pd.ExcelFile('Consumption_of_Residual_Fuel_Oil_for_Bunkering_(Thousand_Barrels_Per_Day).xls')
bunkering = bunkering.parse('Data3')

distillation_capacity = pd.ExcelFile('Crude_Oil_Distillation_Capacity_(Thousand_Barrels_Per_Cal_Day).xls')
distillation_capacity = distillation_capacity.parse('Data3')

reserves = pd.ExcelFile('Crude_Oil_Proved_Reserves_(Billion_Barrels).xls')
reserves = reserves.parse('Data3')

gross_heat_content = pd.ExcelFile('Gross_Heat_Content_of_Crude_Oil_Production_(Thousand_Btu_per_Barrel).xls')
gross_heat_content = gross_heat_content.parse('Data3')

total_exports = pd.ExcelFile('Total_Exports_of_Refined_Petroleum_Products_(Thousand_Barrels_Per_Day).xls')
total_exports = total_exports.parse('Data3')

total_imports = pd.ExcelFile('Total_Imports_of_Refined_Petroleum_Products_(Thousand_Barrels_Per_Day).xls')
total_imports = total_imports.parse('Data3')

total_supply = pd.ExcelFile('Total_Oil_Supply_(Thousand_Barrels_Per_Day).xls')
total_supply = total_supply.parse('Data3')

total_consumption = pd.ExcelFile('Total_Petroleum_Consumption_(Thousand_Barrels_Per_Day).xls')
total_consumption = total_consumption.parse('Data3')

total_petroleum_stocks = pd.ExcelFile('Total_Petroleum_Stocks,_End_of_Period_(Millions_Barrels).xls')
total_petroleum_stocks = total_petroleum_stocks.parse('Data3')

comp = pd.concat([total_imports, total_exports], axis=1)
print comp[2003.0].diff