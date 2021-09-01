import re
import sys

filename = '../../app/routes.py'
f = open(filename, 'r')
content = f.read()
found = re.search('Github\(\'.+\'\)', content)
if found:
    sys.exit('github personal token found')