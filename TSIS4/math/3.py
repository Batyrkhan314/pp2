'''Write a Python program to calculate the area of regular polygon.'''
import math

s = float(input("Number of sides: "))
l = float(input("The length of the side: "))

n = math.tan(math.radians((((s-2)*180)/(2*s))))

area = ((l**2)*n*s)/4

print((area))


