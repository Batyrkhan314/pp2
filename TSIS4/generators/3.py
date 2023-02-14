'''Define a function with a generator which can iterate the numbers, 
which are divisible by 3 and 4, between a given range 0 and n.'''


def gen(n):
    var = 1

    while var<n:
        if var % 3==0 and var%4==0:
            yield var

        var+=1


def counter(n):
    for x in gen(n):
        print(x)

n=int(input())
counter(n)
