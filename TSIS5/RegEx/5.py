'''Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.'''


import re

text = input()
p = 'a.*?b$'
if re.search(p, text):
    print('matches')
else:
    print('Not matches')