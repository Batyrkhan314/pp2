'''Write a Python program to print yesterday, today, tomorrow.'''
import datetime

x = datetime.datetime.now()

y = datetime.datetime(x.year, x.month, x.day-1)
t = datetime.datetime(x.year,x.month, x.day+1)


print("Yesterday: " + str(y))
print("Tomorrow: " + str(t))
