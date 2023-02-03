from functions1_1 import changer
from functions1_4 import isprime

'''considering all elements in input list as mass in grams i want to change prime weights to ounces'''


a = list(map(int,input().split()))

for i in a:
    if isprime(i):
        i = changer(i)
        print(i,end=" ")
    else:
        print(i,end=" ")

