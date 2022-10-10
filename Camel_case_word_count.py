a=input()
c=0
for i in a:
    if(ord(i)>=65 and ord(i)<=90):
        c+=1
if(ord(a[0])>=97 and ord(a[0])<=122):
    c+=1
print(c)