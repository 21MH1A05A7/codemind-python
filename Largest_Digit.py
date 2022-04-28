n=int(input())
#print(n)
s=0
while(n):
    r=n%10 #7 8 9 1
    #print(r)
    if(r>s):
        s=r
    n=n//10
print(s)#3 < 9 