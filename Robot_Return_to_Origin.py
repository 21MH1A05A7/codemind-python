n=input()
s=[]
for i in n:
    s.append(i)
n1=s.count('U')
n2=s.count('D')
n3=s.count('R')
n4=s.count('L')
if(n1==n2 and n3==n4):
    print("True")
else:
    print("False")