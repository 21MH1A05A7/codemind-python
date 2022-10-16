n=input()
rem=n.replace(" ","")
k=rem.lower()
s=set(k)
l=[]
for i in s:
    l.append(i)
l.sort()
for i in l:
    print(i,end="")

