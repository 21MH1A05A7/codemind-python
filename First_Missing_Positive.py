n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(1,max(arr)+1):
    if(i not in arr):
        print(i)
        c=1
        break
if(c==0):
    print(max(arr)+1)
