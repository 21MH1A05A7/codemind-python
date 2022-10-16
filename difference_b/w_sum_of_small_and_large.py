n=input()
s=n.split()
ma=mi=0
for i in s:
    mi+=ord(min(i))
for i in s:
    ma+=ord(max(i))
print(abs(ma-mi))