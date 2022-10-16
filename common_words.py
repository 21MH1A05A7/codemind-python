n1=input()
n2=input()
n3=n1.lower()
n4=n2.lower()
l1=n3.split()
l2=n4.split()
#print(l1)
#print(l2)
for i in l2:
    if(i in l1):
        print(i,end=" ")