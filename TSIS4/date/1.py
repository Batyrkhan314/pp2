'''Write a Python program to subtract five days from current date.'''

import datetime

x = datetime.datetime.now()

y = datetime.datetime(x.year, x.month, x.day-5)

print(y)