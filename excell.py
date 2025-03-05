import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet= wb['Sheet1']
cell = sheet ['b2']


for raw in range(1,sheet.max_row + 1):
    cell=sheet.cell(raw,3)
    print(cell.value)
#printing values of each cell