n=int(input())
arr=list(map(int,input().split()))
q=set(arr)
s=0
for i in q:
    if(arr.count(i)==1 and i%2!=0):
        #print(i)
        s+=1
    elif(arr.count(i)>1 and i%2!=0):
        s+=1
        #print(i)
        arr.remove(i)
print(s)