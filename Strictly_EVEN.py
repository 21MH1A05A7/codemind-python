n=int(input())
arr=list(map(int,input().strip().split()))[:n]
c=0
s=0
for i in range(n):
    if(i%2==0 and arr[i]%2==0):
        c+=1
    if(arr[i]%2==0):
        s+=1
if(s==c):
    print("True")
else:
    print("False")