def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True #prime check
n=int(input())
for i in range(n):
    a=int(input())
    temp=a
    t1=a
    while(True):
        if(prime(a)):
            f=a
            break
        else:
            a=a+1
    while(True):
        if(prime(temp)):
            k=temp
            break
        else:
            temp=temp-1
    if(f-t1<t1-k):
        print(f)
    else:
        print(k)