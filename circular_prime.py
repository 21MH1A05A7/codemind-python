n=int(input())
p=str(n)
q=int(p[::-1])#71
f=0
g=0
for i in range(2,n//2+1):
    if(n%i==0):
        f=1
        break
for j in range(2,q//2+1):
    if(q%j==0):
        g=1
        break
if(f==0 and g==0):
    print("circular prime")
elif(f==0 and g==1):
    print("prime but not a circular prime")
elif(f==1):
    print("not prime")