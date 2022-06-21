n=int(input())
for i in range(n):
    a=input() # h a r s h a
    q=a[::-1] #a[0:0:-1]
    if(a==q and len(a)%2==0):
        print("YES EVEN")
    elif(a==q and len(a)%2!=0):
        print("YES ODD")
    else:
        print("NO")