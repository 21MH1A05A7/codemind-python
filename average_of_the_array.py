n=int(input())
s=0
a=list(map(int,input().strip().split()))[:n]
for i in range(n):
    s=s+a[i]
av=s/n
print("{:.2f}".format(av))