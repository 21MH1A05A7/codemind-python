n=int(input())
arr=list(map(int,input().strip().split()))[:n]
s1=0
s2=0
for i in range(n//2):
    s1+=arr[i]
for j in range(n//2,n):
    s2+=arr[j]
print(s1)
print(s2)
