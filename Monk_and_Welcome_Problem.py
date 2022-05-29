n=int(input())
arr=list(map(int,input().strip().split()))[:n]
l=list(map(int,input().strip().split()))[:n]
a=[]
for i in range(n):
    s=arr[i]+l[i]
    a.append(s)
print(*a)