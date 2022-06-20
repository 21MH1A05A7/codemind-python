n=int(input())
s=[]
j=0
for i in range(n):
    a=int(input())
    while(a):
        r=a%2
        s.append(r)
        a=a//2
    #print(s)
    for i in range(len(s)-1,-1,-1):
        print(s[i],end="")
    print()
    s=[]
    
    