n=input()
q=n.split()
max=len(q[0])
for i in q:
    if(len(i)>max):
        max=len(i)
print(max)