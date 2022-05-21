def palin(n):
    q=str(n)
    if(q==q[::-1]):
        return True
    else:
        return False
def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
if(n>=10 and n<=10000):
    for i in range(1,10000):
        if(palin(n+i) and prime(n+i)):
            
            print(n+i)
            break
    