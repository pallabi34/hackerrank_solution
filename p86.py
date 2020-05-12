t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    d=1
    for i in range(1,n):
        if(l[i]-l[i-1]>2):
            c+=1
        else:
            d+=1
    if(c==0):
        c=n
        
    print(c,d)    
        
            
            
       
        
    
