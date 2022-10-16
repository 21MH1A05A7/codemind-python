n=input()
k=n.replace(" ","")
l=["a","e","i","o","u"]
s=set(k)
for i in s:
    if(i in l):
        l.remove(i)
if(len(l)==0):
    print("True")
else:
    print("False")