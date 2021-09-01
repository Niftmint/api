import re

filename = 'app/routes.py'
f = open(filename, 'r')
content = f.read()
found = re.search('Github\(\'.+\'\)', content)
if found:
    print('\ngithub access token found\n')
    exit(1)
