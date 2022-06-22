n=int(input())
s=0
for i in range(n):
    a=input()
    if('+' in a):
        s=s+1
    elif('-' in a):
        s=s-1
print(s)