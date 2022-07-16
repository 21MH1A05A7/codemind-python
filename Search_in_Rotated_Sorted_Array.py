n=int(input())
arr=list(map(int,input().split()))
f=0
k=int(input())
for i in arr:
    if(i==k):
        print(arr.index(i))
        f=1
        break
if(f==0):
    print("-1")