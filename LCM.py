n,m=map(int,input().split())
if(m>n):
    if(m%n==0):
        print(m)
    else:
        for i in range(2,100):
            if((m*i)%n==0):
                print(m*i)
                break
    