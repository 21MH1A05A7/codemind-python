n=int(input())
arr=list(map(int,input().split()))
l=[]
l1=[]
for i in range(n-1):
    l1.extend(arr[i+1:n])
    m=max(l1)
    l.append(m)
    l1=[]
l.append(-1)
print(*l)