n=int(input())
arr=list(map(int,input().split()))
x=0
c=0
m=max(arr)
for i in range(m,1,-1):
    for j in range(n):
        if(arr[j]%i==0):
            c+=1
    if(c==n):
        print(i)
        x=1
        break
    c=0
if(x==0):
    print("1")