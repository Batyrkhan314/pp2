'''Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
 How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):'''


def finder(numheads,numlegs):
    x=int((numlegs/2-numheads))
    y=int(2*numheads-numlegs/2)

    list = [x,y]
    return list

h = int(input("Number of heads: "))
l = int(input("Number of legs: "))

res = finder(h,l)

print("Number of rabbits: " + str(res[0]))
print("Number of chickens: " + str(res[1]))