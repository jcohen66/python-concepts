import openpyxl

# Create a new workbook and add a worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Add some data to the worksheet
worksheet['A1'] = 'Item'
worksheet['B1'] = 'Quantity'
worksheet['C1'] = 'Price'
worksheet['D1'] = 'Total'

worksheet['A2'] = 'Apples'
worksheet['B2'] = 10
worksheet['C2'] = 2.5
worksheet['D2'] = '=B2*C2'

worksheet['A3'] = 'Pears'
worksheet['B3'] = 5
worksheet['C3'] = 3
worksheet['D3'] = '=B3*C3'

# Save the workbook
workbook.save('report.xlsx')