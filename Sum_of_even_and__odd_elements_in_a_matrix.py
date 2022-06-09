r,c=map(int,input().split())
l=[]
se=0
so=0
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
for i in range(r):
    for j in range(c):
        if(l[i][j]%2==0):
            se+=l[i][j]
        else:
            so+=l[i][j]
print(se,so)
    