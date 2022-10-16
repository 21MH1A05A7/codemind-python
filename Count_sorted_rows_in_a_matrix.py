n,m=map(int,input().split())
l=[]
for i in range(n):
    arr=list(map(int,input().split()))
    l.append(arr)
c=c1=c2=0
for i in range(n):
    for j in range(m-1):
        if(l[i][j]<l[i][j+1]):
            c+=1
        else:
            c2+=1
    if(c==m-1 or c2==m-1):
        c1+=1
    c=0
    c2=0
print(c1)
