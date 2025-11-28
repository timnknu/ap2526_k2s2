import docx

new_doc = docx.Document()
new_doc.add_paragraph().add_run('Here is my new small table')

t = new_doc.add_table(rows = 2, cols = 5)
#new_r = t.add_row()
t.cell(1,1).text = 'SAMPLE'
new_doc.save('generated_table.docx')


d = docx.Document('big_table.docx')
tbl = d.tables[0]
for row in tbl.rows:
    print(row.cells[0].text)