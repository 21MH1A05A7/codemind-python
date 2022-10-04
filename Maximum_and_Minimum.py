n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
l=[]
for i in s:
    if(arr.count(i)==i):
        l.append(i)
if(len(l)==0):
    print("-1")
else:
    print(min(l),max(l))