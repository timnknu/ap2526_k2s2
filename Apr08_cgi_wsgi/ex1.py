
templ = "This is my {w0} {w1} template"

print(templ.format(w1 = 'great', w0 = 'new'))

d = {'w1': 'great', 'w0': 'new'}
print(templ.format(**d))

print(vars())

w0 = 'very new'
w1 = 'fantastic'

print(templ.format(**vars()))
