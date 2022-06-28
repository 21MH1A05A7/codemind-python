n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=set(arr)
l=[]
for i in s:
    if(arr.count(i)==k):
        l.append(i)
if(len(l)==0):
    print("-1")
else:
    print(*l)
