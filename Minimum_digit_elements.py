def count(n):
    q=str(n)
    return len(q)
n=int(input())
arr=list(map(int,input().split()))
c=0
l=[]
for i in range(n):
    b=count(arr[i])
    l.append(b)
mi=min(l)
for i in arr:
    if(count(i)==mi):
        c+=1
print(c)