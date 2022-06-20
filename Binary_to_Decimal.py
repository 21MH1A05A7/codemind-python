n=int(input())
j=0
s=0
for i in range(n):
    a=int(input())
    while(a):
        r=a%10
        s=s+(r*(2**j))
        j+=1
        a=a//10
    print(s)
    s=0
    j=0

    
    