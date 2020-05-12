n=int(input())
x1=list(map(int,input().split()))
x2=list(map(int,input().split()))
min1,min2,min3=1000000,1000000,1000000
for i in range(n):
    if x2[i]==1:
        if x1[i]<min1:
            min1=x1[i]
    elif x2[i]==2:
        if x1[i]<min2:
            min2=x1[i]
    else:
        if x1[i]<min3:
            min3=x1[i]
if  min1+min2 < min3:
    print(min1+min2)
else:
    print(min3)
    
    
        
            
    
