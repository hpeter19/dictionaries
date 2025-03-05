import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet= wb['Sheet1']
cell = sheet ['b2']
print(cell.value)
#checking the value of a cell