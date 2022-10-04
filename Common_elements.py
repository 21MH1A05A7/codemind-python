n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
#print(a)
#print(b)
l=[]
for i in range(n):
    if(a[i] in b and a[i] not in l):
        l.append(a[i])
print(*l)