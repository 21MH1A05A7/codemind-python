n=int(input())
arr=list(map(int,input().strip().split()))[:n]
m=arr[0]
for i in range(1,len(arr)):
    if(arr[i]<m):
        m=arr[i]
print(m)
    