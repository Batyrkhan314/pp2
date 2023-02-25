'''Write a Python program to find sequences of lowercase letters joined with a underscore.'''

import re

text = input()
p = '^[a-z]+_[a-z]+$'
if re.search(p,  text):
    print('matches')
else:
    print('not matches')