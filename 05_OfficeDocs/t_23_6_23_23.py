import docx
import re

RE_PATT = r'(?P<prefix>[^\d])(?P<num>\.\d{1,})'
d = docx.Document('sample2.docx')
color_to_replace = docx.shared.RGBColor.from_string('CC0000')
new_color = docx.shared.RGBColor.from_string('1f2d99')
for par in d.paragraphs:
    print('-'*80)
    for r in par.runs:
        if r.font.color.rgb == color_to_replace:
            print('RUN:', r.text, type(r.font.color.rgb), docx.shared.RGBColor(1,1,1))
            def my_repl_func(m):
                before_dot = m.groupdict()['prefix']
                dot_and_digits = m.groupdict()['num']
                return before_dot + '0' + dot_and_digits

            new_text = re.sub(RE_PATT, my_repl_func, r.text)
            r.text = new_text
            r.font.color.rgb = new_color

d.save('new_doc1.docx')
