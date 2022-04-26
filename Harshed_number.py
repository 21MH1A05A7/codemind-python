n=int(input())
s=0
for i in str(n):
    s=s+int(i)
if(n%s==0):
    print("True")
else:
    print("False")