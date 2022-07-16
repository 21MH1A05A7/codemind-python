n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
for i in s:
    if(arr.count(i)>1):
        print(i)
        break