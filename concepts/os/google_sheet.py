# Get your API : https://console.cloud.google.com/
# pip install gspread
import gspread as sheet
gs = sheet.service_account()
# Open Sheet 
wb = gs.open("Sheet 1")
wb = wb.sheet1
# fetch all rows
rows = wb.get_all_records()
# fetch all columns
coloums = wb.get_all_values()
# fetch specific row
row = wb.row_values(1)
# fetch specific column
column = wb.col_values(1)
# Get specific cell
cell = wb.cell(1,1).value
# write to cell
wb.update_cell(3,2,"medium")