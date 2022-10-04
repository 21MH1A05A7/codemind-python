def prime(n):
    if(n==1):
        return False
    else:
        for i in range(2,n//2+1):
            if(n%i==0):
                return False
        else:
            return True
n=int(input())
arr=list(map(int,input().split()))
#print(arr)
k=int(input())
#print(k)
c=0
for i in range(n):
    if(arr[i]>=k):
        if(prime(arr[i])):
            c+=1
print(c)
