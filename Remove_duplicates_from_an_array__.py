n=int(input())
arr=list(map(int,input().split()))[:n]
arr=list(dict.fromkeys(arr))
for i in range(n):
    print(arr[i],end=" ")