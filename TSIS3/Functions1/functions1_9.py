'''9. Write a function that computes the volume of a sphere given its radius.
'''
import math

def volume(rad):
    return float((4/3)*math.pi*rad**3)


n = int(input())
print(volume(n))