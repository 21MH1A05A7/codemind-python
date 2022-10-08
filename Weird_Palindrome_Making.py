import math
t=int(input())
for j in range(t):

    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in arr:
        if(i%2==1):
            c+=1
    print(c//2)