n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if(i==0):
        c+=1
    if(i<0): # -24 --->24
        i=i*-1
    while(i): # 24,2
                # 1,.....2
        i=i//10 #2,..0
        c+=1
    print(c,end=" ")
    c=0