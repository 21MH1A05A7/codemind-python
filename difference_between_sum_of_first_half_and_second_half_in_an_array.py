n=int(input())
arr=list(map(int,input().strip().split()))[:n]
s1=0
s2=0
if(n%2==0):
    for i in range(n//2):
        s1+=arr[i]
    for j in range(n//2,n):
        s2+=arr[j]
    print(abs(s1-s2))
else:
    arr.append(arr[n-1]+1)
    for i in range(n//2):
        s1+=arr[i]
    for j in range(n//2,n):
        s2+=arr[j]
    print(abs(s1-s2))
