char=list(input())
n=len(char)
for i in range(n//2):
    temp=char[i]
    char[i]=char[n-i-1]
    char[n-i-1]=temp
for i in range(n):
    print(char[i],end="")
    