n,k,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(k):
    arr.insert(0,arr[-1])
    arr.pop(-1)
for i in range(q):
    s=int(input())
    print(arr[s])