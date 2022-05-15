n=input()
l=['a','e','i','o','u']
for i in n:
    if(i in l):
        l.remove(i)
if(len(l)==0):
    print("0")
for i in l:
    print(i,end=" ")