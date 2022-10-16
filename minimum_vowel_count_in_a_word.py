n=input()
s=n.split()
c=0
l=[]
for i in s:
    for j in i:
        #print(j)
        if j in "aeiou":
            c+=1
    l.append(c)
    c=0
print(min(l))