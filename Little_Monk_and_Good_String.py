n=input()
c=0
res=0
for i in n:
    if i in  "aeiou":
        c+=1
    else:
        res = max(res,c)        
        c=0
print(max(res,c))