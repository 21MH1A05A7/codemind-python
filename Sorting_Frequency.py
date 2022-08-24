d={}
n=int(input())
arr=list(map(int,input().split()))[:n]
s=set(arr)
for i in s:
    c=arr.count(i)
    d[i]=c
l=[]
for i in range(len(d)):
    m=0
    for i in d.keys():
        if(d[i]>m):
            m=d[i]
            k=i
    l.append(k)
    d.pop(k)
print(*l)
