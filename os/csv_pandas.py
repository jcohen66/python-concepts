# CSV Data Entry
# pip install pandas
import pandas as pd
# Load and Read CSV File
csv = pd.read_csv('organizations-10000.csv')
# Print Whole CSV data
print(csv)
# Print Specific Columns
print(csv['column1', 'column2'])
# Print Specific Rows
print(csv.loc[0:2])
# Print Specific Rows and Columns
print(csv.loc[0:2, 'column1', 'column2'])
# Print Specific Cell
print(csv.loc[0, 'column1'])
# Write to Specific Cell
csv.loc[0, 'column1'] = 'new value'
# Write to Specific Rows and Columns
csv.loc[0:2, 'column1', 'column2'] = 'new value'
# Append new Data
csv = csv.append({'column3': 'value1'}, ignore_index=True)
# Delete Specific Rows
csv = csv.drop(0)
# Delete Specific Columns
csv = csv.drop('column1', axis=1)
# Remove Duplicates
csv = csv.drop_duplicates()
# Sort Data
csv = csv.sort_values('column1', ascending=False)
# Filter Data
csv = csv[csv['column1'] == 'value1']
# Filter Data with Multiple Conditions
csv = csv[(csv['column1'] == 'value1') & (csv['column2'] == 'value2')]
# Add New Column
csv['new_column'] = 'new value'
# Save CSV File
csv.to_csv('file.csv', index=False)