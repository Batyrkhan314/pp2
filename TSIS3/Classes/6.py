

arr= list(map(int,input().split()))

l = list(filter(lambda x :  all(x % i !=0 for i in range(2,int(x/2)+1)),arr))

print(l)
