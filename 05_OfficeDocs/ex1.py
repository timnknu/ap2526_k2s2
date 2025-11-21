import openpyxl

wb = openpyxl.load_workbook('sample_src_table.xlsx')
#print(wb.sheetnames)
wsheet = wb[wb.sheetnames[0]]

for i in range(3, wsheet.max_row+1):
    x = wsheet.cell(row=i, column=1).value
    wsheet.cell(row=i, column=2).value = x**2

wb.save('sample_edited1.xlsx')
