def palin(n):
    q=str(n)
    if(q==q[::-1]):
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(palin(i)):
        print(i,end=" ")
    