r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))
    l.append(arr)
t=[]
s=0
for i in range(c):
    for j in range(r):
        s+=l[j][i]
    t.append(s)
    s=0
print(max(t))