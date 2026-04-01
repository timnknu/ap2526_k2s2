import urllib.parse

qs = "http://localhost:15555/processdata?key=hello+%D1%81%D0%B2%D1%96%D1%82&valueofx=76786&valueofx=12"

s = urllib.parse.urlsplit(qs)
print(s.path)
print(s.query)

r = urllib.parse.parse_qs(s.query)

print(r)