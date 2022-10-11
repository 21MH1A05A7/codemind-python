n,m=map(int,input().split())
arr=list(map(int,input().split()))
l=list(map(int,input().split()))
#print(arr)
#print(l)
s1=set(arr)
s2=set(l)
c=0
c_v=0

for i in s1:
    for j in s2:
        if(i!=j):
            c_v+=1
    if(c_v==len(s2)):
        #print(i)
        c+=1
    c_v=0
for i in s2:
    for j in s1:
        if(i!=j):
            c_v+=1
    if(c_v==len(s1)):
        #print(i)
        c+=1
    c_v=0
print(c)
                