n=int(input())
arr=list(map(int,input().strip().split()))[:n]
a=int(input())
f=0
for i in range(len(arr)):
    if(arr[i]==a):
        f=1
        break
if(f==1):
    print("True")
else:
    print("False")