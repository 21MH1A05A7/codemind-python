t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=[]
    if(n%2==0):
        for i in range(n//2):
            l.append(arr[n-i-1])
            l.append(arr[i])
    else:
        for i in range(n//2):
            l.append(arr[n-i-1])
            l.append(arr[i])
        l.append(arr[n//2])
    print(*l)
    