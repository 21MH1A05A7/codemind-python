n=input()
q=n.split()
for i in range(len(q)):
    p=q[i]
    r=p[::-1]
    q[i]=r
for i in range(len(q)):
    print(q[i],end=" ")