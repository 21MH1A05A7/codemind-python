n=int(input())
temp=n+1
for i in range(n):
    for j in range(1,temp):
        print(j,end="")
    print()
    temp-=1
    