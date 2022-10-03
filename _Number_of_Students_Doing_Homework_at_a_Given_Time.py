n=int(input())
arr=list(map(int,input().split()))
#print(arr)
m=int(input())
l=list(map(int,input().split()))
#print(l)
q_time=int(input())
c=0
for i in range(n):
    if(q_time in range(arr[i],l[i]) or q_time==l[i]):
        c+=1
print(c)