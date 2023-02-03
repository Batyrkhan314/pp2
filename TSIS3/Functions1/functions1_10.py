'''10.Write a Python function that takes a list and returns a new list with unique elements of the first list. 
Note: don't use collection set.
'''

def checker(n,i,arr):
    if i<(len(arr)-2):
        for j in range(i+1,len(arr)):
            if arr[j]==n:
                return False

    return True

def adder(arr):
    l = []

    for i in range(len(arr)):
        if checker(arr[i],i,arr)==True:
            l.append(a[i])

    return l


a = list(map(int,input().split()))

print(adder(a))