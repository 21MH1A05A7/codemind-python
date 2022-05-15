n=input()
q=n.split()
for i in range(len(q)):
    if(i%2==0):
        p=q[i]
        r=p[::-1]
        q[i]=r
for i in q:
    print(i,end=" ")