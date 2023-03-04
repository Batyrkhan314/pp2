'''Write a Python program with builtin function to multiply all the numbers in a list'''

import math

l = [int(s) for s in input().split()]

print(math.prod(l))