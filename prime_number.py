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
if(prime(n)):
    print("prime")
else:
    print("not a prime")