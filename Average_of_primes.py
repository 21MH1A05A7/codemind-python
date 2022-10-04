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
l=[]
for i in arr:
    if(prime(i)):
        l.append(i)
print("{:.2f}".format(sum(l)/len(l)))