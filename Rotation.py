t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(k):
        f=arr[-1]
        arr.insert(0,f)
        arr.pop()
    print(*arr)