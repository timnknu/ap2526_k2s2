import docx

d = docx.Document('big_table.docx')
tbl = d.tables[0]
for row in tbl.rows:
    print(row.cells[0].text)