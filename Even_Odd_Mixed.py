n=int(input())
ce=0
co=0
for i in str(n):
    if(int(i)%2==0):
        ce+=1
    else:
        co+=1
if(ce==len(str(n))):
    print("Even")
elif(co==len(str(n))):
    print("Odd")
else:
    print("Mixed")