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
k=int(input())
c=0
for i in arr:
    if(i<=k):
        if(prime(i)):
            c+=1
print(c)