n=int(input())
arr=list(map(int,input().split()))
q=set(arr)
s=0
for i in q:
    if(arr.count(i)==1 and i%2!=0):
        #print(i)
        s+=i
    elif(arr.count(i)>1 and i%2!=0):
        s+=i
        #print(i)
        arr.remove(i)
print(s)