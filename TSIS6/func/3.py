'''Write a Python program with builtin function that checks whether a passed string is palindrome or not.'''

s = input()


if list(reversed(s)) == list(s):
    print('True')
else:
    print('False')