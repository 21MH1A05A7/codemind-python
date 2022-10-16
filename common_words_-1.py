n=input()
m=input()
lw1=n.lower()
lw2=m.lower()
l1=lw1.split()
l2=lw2.split()
c=0
for i in l2:
    for j in l1:
        if(i==j):
            c+=1
print(c)