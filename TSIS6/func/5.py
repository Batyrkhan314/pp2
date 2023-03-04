'''Write a Python program with builtin function that returns True if all elements of the tuple are true.'''

t = (False, 0 ,1)

if all(t):
    print("True")
else:
    print("False")