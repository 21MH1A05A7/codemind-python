n=int(input())
arr=list(map(int,input().split()))
n_l=[]
c_l=[]
c=0
for i in range(n):
    for j in range(n):
        if(arr[i] not in n_l):
            n_l.append(arr[i])
#print(n_l)
for i in n_l:
    c_l.append(arr.count(i))
#print(c_l)

for i in range(len(c_l)):
    print(n_l[i],end=" ")
    print(c_l[i],end=" ")
'''arr.sort()
s=set(arr)
for i in s:
    l.append(i)
    l.append(arr.count(i))
print(*l)'''



