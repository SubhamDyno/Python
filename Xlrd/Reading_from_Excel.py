import xlrd

path =  ".\First.xlsx"

wb = xlrd.open_workbook(path);
sheet = wb.sheet_by_index(0);

for j in range(sheet.ncols):
    for i in range(sheet.nrows):
       map(sheet.cell_value(i,j))
