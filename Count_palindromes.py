n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
for i in range(n):
    q=str(arr[i])
    r=q[::-1]
    s=int(r)
    if(s==arr[i]):
        c+=1
print(c)