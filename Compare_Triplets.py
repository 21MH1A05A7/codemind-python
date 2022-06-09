a=list(map(int,input().split()))
b=list(map(int,input().split()))
ca=0
cb=0
for i in range(len(a)):
    if(a[i]>b[i]):
        ca+=1
    elif(a[i]<b[i]):
        cb+=1
print(ca,cb)