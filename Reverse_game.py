def palin(n):
    q=str(n)
    return q[::-1]
n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    b=palin(i)
    l.append(int(b))
print(*l)