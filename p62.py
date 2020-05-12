n=int(input())
arr=list(map(int,input().split()))
k=n//2
arr.sort()
a=0
for i in range(1,k+1):
    if(arr[i-1]<arr[i]):
        a=arr[i]
        
print(a)    
       
