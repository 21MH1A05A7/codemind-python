n=input()
q=n.split()
for i in range(len(q)):
    p=q[i]
    r=p[::-1]
    q[i]=r
#print(q)
a=len(q)
for i in range(a-1,-1,-1):
    print(q[i],end=" ")