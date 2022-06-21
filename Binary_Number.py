n=int(input())
l=[]
for i in range(0,pow(2,n)):
    while(i):
        r=i%2
        l.append(r)
        i=i//2
    if(len(l)<n):
        for i in range(n-len(l)):
            l.append(0)
    for i in range(len(l)-1,-1,-1):
        print(l[i],end="")
    print()
    l=[]
