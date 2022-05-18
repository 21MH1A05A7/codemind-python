n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
for i in range(n):
    if(arr[i]+1<=n):
        c+=1
if(c==len(arr)):
    print("YES")
else:
    print("NO")