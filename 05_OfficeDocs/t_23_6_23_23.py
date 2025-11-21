import docx


d = docx.Document('sample2.docx')
color_to_replace = docx.shared.RGBColor.from_string('CC0000')
new_color = docx.shared.RGBColor.from_string('1f2d99')
for par in d.paragraphs:
    print('-'*80)
    for r in par.runs:
        if r.font.color.rgb == color_to_replace:
            print('RUN:', r.text, type(r.font.color.rgb), docx.shared.RGBColor(1,1,1))
            r.font.color.rgb = new_color
d.save('new_doc1.docx')
