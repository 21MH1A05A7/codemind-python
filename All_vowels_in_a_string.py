n=input()
l=['a','e','i','o','u']
a=['A','E','I','O','U']
k=[]
q=[]
c=0
s=0
for i in n:
    if(i in l and i not in k):
        c+=1
        k.append(i)
    elif(i in a and i not in q):
        s+=1
        q.append(i)
if(c==len(l) or s==len(a)):
    print(True)
else:
    print(False)