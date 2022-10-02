n=int(input())
i=1
t_power=1 # 2 power 
l=[]
while(t_power<n):
    t_power=2**i
    i+=1
    l.append(abs(t_power-n))
print(min(l))