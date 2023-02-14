'''Create a generator that generates the squares of numbers up to some number N.'''


n = int(input())

def sq_gen(n):

    val = 0

    while val < n+1:
         yield val**2

         val+=1

for x in sq_gen(n):
    print(x)