n=int(input())
arr=list(map(int,input().split()))[:n]
s1=0
s2=0
for i in range(n//2):
    s1+=arr[i]
for i in range(n//2,n):
    s2+=arr[i]
print(s1)
print(s2)