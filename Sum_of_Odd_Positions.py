n=int(input())
s=0
a = list(map(int,input().strip().split()))[:n]
for i in range(0,len(a)):
    if(i%2!=0):
        s=s+a[i]
print(s)