n,k=map(int,input().split())
arr=list(map(int,input().split()))
#print(arr)
l=[]
for i in range(k):
    arr.append(arr[0])
    arr.pop(0)
print(*arr)