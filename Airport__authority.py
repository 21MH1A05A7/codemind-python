n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
k=int(input())
s=0
#print(arr)
for i in range(n):
    if(arr[i]<=k):
        s+=1
    else:
        s+=2
print(s)