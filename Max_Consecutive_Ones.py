n=int(input())
arr=list(map(int,input().split()))
c=0
m=0
for i in range(n):
    if(i==n-1):
        if(arr[i]==1):
            c+=1
        if(c>m):
            m=c
    elif(arr[i]==0):
        if(c>m):
            m=c
        c=0
    else:
        c+=1

print(m)