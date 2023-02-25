'''Write a Python program that matches a string that has an 'a' followed by two to three 'b'.'''

import re


text = input()
p = 'ab{2,3}'
if re.search(p,  text):
    print('matches')
else:
    print('Not matches')
