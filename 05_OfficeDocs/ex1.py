import openpyxl

wb = openpyxl.load_workbook('sample_src_table.xlsx')
print(wb.sheetnames)
wsheet = wb[wb.sheetnames[0]]

# for i in range(1, 20):
#     print(wsheet.cell(row=i, column=1).value)
for r in wsheet.iter_rows():
    print(r)
print(wsheet.max_row, wsheet.max_column)