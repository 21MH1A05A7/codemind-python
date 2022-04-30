n=int(input())
count=0
for i in range(n):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        r=j%10
        if(r==2 or r==3 or r==9):
            count+=1
    print(count)
    count=0