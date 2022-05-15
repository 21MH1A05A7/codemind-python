n=input()
q=n.split()
min=len(q[0])
for i in q:
    if(len(i)<min):
        min=len(i)
print(min)