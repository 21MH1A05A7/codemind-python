n=int(input())
arr=list(map(int,input().split()))
#print(arr)
s=0
for i in arr:
    for j in str(i):
        s=s+int(j)
print(s)