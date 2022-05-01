n=int(input())
arr=list(map(int,input().split()))[:n]
se=0
so=0
for i in range(n):
    if(i%2==0):
        se+=arr[i]
    else:
        so+=arr[i]
if(abs(so-se)==0):
    print("YES")
else:
    print("NO")