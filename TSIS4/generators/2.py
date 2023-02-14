'''Write a program using generator to print the even numbers between 0 and n in
 comma separated form where n is input from console.'''

def gen(n):

    var=0

    while var<n:

        if var%2==0:
            if var != n-2:
                string = str(var) + ","
                yield string
            else : 
                yield var

        var+=1


n = int(input())

for x in gen(n):
    print(x,end=" ")