def count(n):
    q=str(n)
    return len(q)

n=int(input())
arr=list(map(int,input().split()))
c=0
max=0
for i in arr:
    b=count(i)
    if(b>max):
        max=b
for i in arr:
    if(len(str(i))==max):
        c+=1
print(c)
    