n=int(input())
a=0
b=1
while(n):
    c=a+b
    if(c>=n):
        d1=c-n
        d2=n-b
        if(d1>d2):
            print(b)
            break
        elif(d1==d2):
            print(b,c)
            break
        else:
            print(c)
            break
    a=b
    b=c