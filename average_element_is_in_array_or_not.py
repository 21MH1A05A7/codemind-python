n=int(input())
s=0
a=list(map(int,input().strip().split()))[:n]
for i in range(n):
    s=s+a[i]
av=s//n
f=0
for i in range(n):
    if(av==a[i]):
        f=1
        break
if(f==1):
    print("True")
else:
    print("False")