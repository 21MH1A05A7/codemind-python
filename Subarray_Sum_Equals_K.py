f=0
m,s=map(int,input().split())
arr=list(map(int,input().split()))
for j in range(m):
    for k in range(j,m):
        if(sum(arr[j:k+1])==s):
            f+=1
print(f)