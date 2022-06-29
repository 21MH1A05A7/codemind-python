n=int(input())
arr=list(map(int,input().split()))
c=0
count=0
for i in range(n):
    if(i%2!=0 and arr[i]%2!=0):
        c+=1
for i in arr:
    if(i%2!=0):
        count+=1
if(count==c):
    print(True)
else:
    print(False)