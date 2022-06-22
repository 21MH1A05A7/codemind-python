n=int(input())
for i in range(n):
    j=0
    k=0
    decnum=0
    binum=[]
    a=int(input())
    while(a):
        r=a%10
        decnum=decnum+(int(r)*8**j)
        j+=1
        a=a//10
    while(decnum):
        r=decnum%2
        binum.append(r)
        decnum=decnum//2
    for i in range(len(binum)-1,-1,-1):
        print(binum[i],end="")
    print()
    decnum=0