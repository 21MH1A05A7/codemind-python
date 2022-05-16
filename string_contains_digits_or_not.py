n=int(input())
for i in range(n):
    a=input()
    for j in a:
        if(j.isdigit()):
            print("Yes")
            break
    else:
        print("No")