n=int(input())
arr=list(map(int,input().strip().split()))[:n]
#print(arr)
l=[]
d=0
for i in range(n):
    p=arr[i]
    if(p==0):
        d+=1
    if(p<0):
        p=p*-1
    while(p):
        d+=1
        p=p//10
    l.append(d)
    d=0
for i in range(n):
    print(l[i],end=" ")