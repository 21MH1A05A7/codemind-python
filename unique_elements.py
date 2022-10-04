n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if(arr.count(i)>=1 and i not in l):
        l.append(i)
print(*l)