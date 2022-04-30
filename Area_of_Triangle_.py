import math
n,m,t=map(int,input().split())
s=(n+m+t)/2
st=math.sqrt(s*(s-n)*(s-m)*(s-t))
print("{:.2f}".format(st))