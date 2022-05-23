import math
n=int(input())
for i in range(n):
    a=int(input())
    q=math.sqrt(a)
    if(q*q==a and a%q==0):
        print(True)
    else:
        print(False)