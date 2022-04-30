n=int(input())
s=0
for i in range(1,n+1):
    p=1/i
    s=s+p
print("{:.2f}".format(s))