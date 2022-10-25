n=int(input())
t=n*2
if(n>=3 and n<=100):
    
    for i in range(t//2):
        for j in range(i+1):
            print("*",end="")
        print()
    for i in range(t//2-1,0,-1):
        for j in range(i):
            print("*",end="")
        print()
else:
    print("The pattern is not possible")