t=int(input())
f=0
for i in range(t):
    m,s=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in range(m-1):
        for k in range(j+1,m):
            if(sum(arr[j:k+1])==s):
                print(j+1,k+1)
                f=1
                break
        if(f==1):
            break
    if(f==0):
        print("-1")
    f=0