'''12. Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
For example, histogram([4, 9, 7]) should print the following:'''

def histogram(arr):
    n = len(arr)
    s = '*'

    for i in range(n):
        print(s*arr[i])


a = list(map(int,input().split()))

histogram(a)

