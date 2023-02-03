'''7.Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
'''


def three(arr):
    n = len(arr)

    for i in range(n):
        if i<n-1:
            if arr[i] == 3 and arr[i+1] == 3:
                return True

    return False


a = list(map(int,input().split()))

print(three(a))

