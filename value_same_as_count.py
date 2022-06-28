n=int(input())
arr=list(map(int,input().split()))
c=0
s=set(arr)
for i in s:
    if(arr.count(i)==i):
        c+=1
print(c)