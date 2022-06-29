n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    if(arr[i]%2!=0):
        l.append(arr[i])
for i in arr:
    if(i%2==0):
        l.append(i)
print(*l)