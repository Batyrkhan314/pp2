'''8. Write a function that takes in a list of integers and returns True if it contains 007 in order
'''

def agent_007(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            for j in range(i+1,n):
                if arr[j]==0:
                    for k in range(j+1,n):
                        if arr[k] == 7:
                            return True

    return False


a = list(map(int,input().split()))

print(agent_007(a))