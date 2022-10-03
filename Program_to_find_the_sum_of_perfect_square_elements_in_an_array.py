n=int(input())
arr=list(map(int,input().split()))
#print(arr)
s=0
for i in arr:
    if(i==1):
        s=s+i
    else:
        for j in range(1,i//2+1):
            if(j*j==i):
                s+=i
                break
print(s)