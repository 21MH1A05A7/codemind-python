n=int(input())
m=int(input())
f=0
if(n==1):
    n=2
for i in range(n,m+1):
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i)
    f=0