n=int(input())
arr=list(map(int,input().strip().split()))[:n]
count=0
for i in range(len(arr)):
    if(arr[i]%2==0):
        count+=1
if(count==len(arr)):
    print("True")
else:
    print("False")