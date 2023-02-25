'''Write a Python program to convert a given camel case string to snake case.'''

from re import sub

text = input()
print('_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    text.replace('-', ' '))).split()).lower())


