import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet= wb['Sheet1']
cell = sheet ['b2']

print(sheet.max_row)
print(sheet.max_column)
#checking the number of rows and columns on a spredsheet