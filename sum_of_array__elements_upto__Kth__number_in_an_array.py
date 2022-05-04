n=int(input())
arr=list(map(int,input().strip().split()))[:n]
m=int(input())
s=0
for i in range(m):
    s=s+arr[i]
print(s)
    