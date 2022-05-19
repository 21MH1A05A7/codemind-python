n=int(input())
arr=list(map(int,input().strip().split()))[:n]
l=[]
c=0
for i in range(n):
    for j in range(n):
        if(arr[i]==arr[j] and arr[i] not in l):
            c+=1
    if(c>=1):
        l.append(arr[i])
    c=0
s=0
for i in range(len(l)):
    s+=l[i]
print(s)