r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
s=0
s1=0
for i in range(r):
    if(i%2!=0):
        for j in range(c):
            s1+=l[i][j]
    else:
        
        for j in range(c):
            s+=l[i][j]
print(s,s1)