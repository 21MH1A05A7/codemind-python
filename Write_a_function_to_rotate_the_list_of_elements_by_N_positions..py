n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for i in range(k):
    f=arr[-1]
    arr.insert(0,f)
    arr.pop()
print(*arr)