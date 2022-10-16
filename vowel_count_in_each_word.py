n=input()
l=n.split()
c=0
for i in l:
    for j in i:
        if(j in "aeiou"):
            c+=1
    
    print(c,end=" ")
    c=0