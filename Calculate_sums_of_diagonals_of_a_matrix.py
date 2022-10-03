n=int(input())
l=[]
for i in range(n):
    arr=list(map(int,input().split()))
    l.append(arr)
sp=0
ss=0
for i in range(n):
    for j in range(n):
        if(i==j):
            sp=sp+l[i][j]
k=n-1
for i in range(n):
    ss+=l[i][j]
    j-=1
print("Principal Diagonal:{}".format(sp))
print("Secondary Diagonal:{}".format(ss))