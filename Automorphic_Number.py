n=int(input())
s=n*n
temp=n
t=s
c=0
while(n): #76
    p=n%10 #6 7  
    #print(p)
    #print(s)
    while(s):#5776  577 57 5
        r=s%10 # 6 7 7 5
        #print(r)
        if(p==r): # 1,
            c+=1 #2
            #print(c)
            break
        s=int(s/10)
    n=int(n/10)
    if(n>=0):
        s=t
    else:
        break
#print(len(str(temp)))
#print(c)
if(len(str(temp))==c):
    print("Automorphic Number")
else:
     print("Not an Automorphic Number")