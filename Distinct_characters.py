n=input()
k=n.replace(" ","")
lw=k.lower()
s=set(lw)

l=[]
for i in s:
    if(lw.count(i)==1):
        l.append(i)
l.sort()
for i in l:
    print(i,end="")