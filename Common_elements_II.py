n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(n):
    if(a[i] not in b and a[i] not in l):
        l.append(a[i])
for j in range(m):
    if(b[j] not in a and b[j] not in l):
        l.append(b[j])
print(*l)