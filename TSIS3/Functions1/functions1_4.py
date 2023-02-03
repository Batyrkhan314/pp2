'''You are given list of numbers separated by spaces. 
Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.'''

def isprime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False

    return True


def checker(arr):
    res = []
    for i in arr:
        if isprime(i)==True:
            res.append(i)

    return res


'''a = list(map(int, input().split()))

outcome = checker(a)

print(outcome)'''
