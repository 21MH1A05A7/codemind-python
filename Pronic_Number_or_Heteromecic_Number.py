n=int(input())
flag=0
for i in range(1,100):
    if(i*(i+1)==n):
        flag=1
        break
if(flag==1):
    print("YES")
else:
    print("NO")
