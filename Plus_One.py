n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    s=s*10+i
ts=s+1
l=[]
for i in str(ts):
    l.append(i)
print(*l)
    