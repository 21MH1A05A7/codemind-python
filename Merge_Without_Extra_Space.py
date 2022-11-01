t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    l=list(map(int,input().split()))
    arr.extend(l)
    arr.sort()
    print(*arr)