n=int(input())
#print(n)
s=0
while(n!=1 or n!=7):
    while(n):
        r=n%10
        s=s+r**2
        n=n//10
    if(s<10):
        n=s
        break
    n=s
    #print(n)
    s=0
if(n==1 or n==7):
    print("True")
else:
    print("False")