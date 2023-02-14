'''Implement a generator called squares to yield the square of all 
numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.'''

arr = [int(x) for x in input().split()]
a,b = arr[0] , arr[1]
gen = (x**2 for x in range(a,b))

for y in  gen:
    print(y)