'''Implement a generator that returns all numbers from (n) down to 0.'''

n = int(input())

gen = (x for x in range(n,-1,-1))

for y in gen:
    print(y)