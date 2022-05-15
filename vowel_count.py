n=input()
q=n.lower()
c=0
l=['a','e','i','o','u']
for i in q:
    if(i in l):
        c+=1
print(c)