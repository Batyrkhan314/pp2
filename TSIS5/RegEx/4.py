import re

text = input()
p = '[A-Z]+[a-z]+$'
if re.search(p, text):
    print('matches')
else:
    print('Not matches')