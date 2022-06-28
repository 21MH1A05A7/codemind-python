n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(len(arr)):
    if(arr[i]>=a and arr[i]<=b):
        l.append(arr[i])
print(sum(l))