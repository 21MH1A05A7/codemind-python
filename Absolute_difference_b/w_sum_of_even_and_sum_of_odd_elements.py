n=int(input())
se=0
so=0
a=list(map(int,input().strip().split()))[:n]
for i in range(0,len(a)):
    if(a[i]%2==0):
        se+=a[i]
    else:
        so+=a[i]
if(se>so):
    print(se-so)
elif(so>se):
    print(so-se)
else:
    print(0)