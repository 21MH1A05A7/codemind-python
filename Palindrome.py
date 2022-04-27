n=int(input())
q=str(n)
if(int(q[::-1])==n):
    print("True")
else:
    print("False")