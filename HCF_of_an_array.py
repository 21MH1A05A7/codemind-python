n=int(input())
arr=list(map(int,input().strip().split()))[:n]
arr.sort()
c=0
for i in range(n):
    if(arr[i]%arr[0]==0):
        c+=1
if(c==n):
    print(arr[0])
else:
    print("1")