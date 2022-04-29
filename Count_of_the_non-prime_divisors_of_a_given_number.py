n=int(input())
#print(n)
count=1
f=0
for i in range(2,n+1):
    
    for j in range(2,i): # 2, 3,4 ,5
        if(i%j==0 and n%i==0):
            f=1
            #print(i)
            break
    if(f==1):
        count+=1
    f=0
print(count)