'''Write a Python program to write a list to a file. '''

l = [s for s in input().split()]

file = open('items.text', 'w')

for x in l:
    file.write(x+" ")

file.close()
