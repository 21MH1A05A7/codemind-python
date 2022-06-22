n=int(input())
for i in range(n):
    a=int(input())
    decnum=0
    j=0
    l=[]
    while(a):
        r=a%10
        decnum=decnum+(r*2**j)
        a=a//10
        j+=1
    while(decnum):
        r=decnum%8
        l.append(r)
        decnum=decnum//8
    for i in range(len(l)-1,-1,-1):
        print(l[i],end="")
    print()
    decnum=0
    l=[]
    