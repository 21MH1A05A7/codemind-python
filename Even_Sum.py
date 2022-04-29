n=int(input())
s=0
a=list(map(int,input().strip().split()))[:n]
for i in range(len(a)):
    if(a[i]%2==0):
        s=s+a[i]
print(s)