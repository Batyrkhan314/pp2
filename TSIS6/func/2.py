'''Write a Python program with builtin function that accepts a string 
and calculate the number of upper case letters and lower case letters'''

s = input()
u=0
l=0
for a in s:
    if a.isupper():
        u +=1
    else:
        l +=1

print(u,l)