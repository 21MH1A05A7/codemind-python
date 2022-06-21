n=input()
l=n.split()
for i in range(len(l)):
    q=l[i]
    r=q[::-1]
    l[i]=r
print(*l)