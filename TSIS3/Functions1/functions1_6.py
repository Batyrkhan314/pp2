'''6.Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
'''

def rev(s):
    temp=""
    l = []

    for ch in s :
        if ch == ' ':
            l.append(temp)
            temp=""
        else:
            temp+=ch


    l.append(temp)

    for i in l[::-1]:
        print(i , end = " ")


string = input()
rev(string)

