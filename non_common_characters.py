n1=input()
n2=input()
l1=n1.lower()
l2=n2.lower()
l=[]
k=' '
c=0
for i in l1:
    if i not in l2 and i not in k and i not in l:
        l.append(i)
for i in l2:
    if i not in l1 and i not in k and i not in l:
        l.append(i)
l.sort()
for i in l:
    print(i,end="")