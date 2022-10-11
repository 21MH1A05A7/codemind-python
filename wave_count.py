def wave(arr):
    
    result = 0
    if (arr[1]>arr[0] and arr[1]>arr[2]):
        for i in range(1,n-1,2):
 
            if (arr[i] > arr[i-1] and arr[i] > arr[i+1]):
                result+=1
         
            else :
                result=0
                break
 
        # Check for last element
        if (result==True and n%2==0):
            if (arr[n-1] <= arr[n-2]) :
                result=0
             
    elif (arr[1]<arr[0] and arr[1]<arr[2]) :
        for i in range(1,n-1,2) :
    
            if (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
                result+=1
             
            else :
                result = 0
                break
 
        # Check for last element
        if (result==True and n%2==0) :
            if (arr[n-1] >= arr[n-2]) :
                result=0
 
    return result
n=int(input())
arr=list(map(int,input().split()))
r=wave(arr)
if(r==0):
    print("-1")
else:
    
    print(r)
#print(c)