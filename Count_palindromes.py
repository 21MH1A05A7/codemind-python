def palin(n):
    q=str(n)
    if(q==q[::-1]):
        return True
    else:
        return False
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(palin(i)):
        c+=1
print(c)