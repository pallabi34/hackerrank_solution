t=int(input())
for i in range(t):
    n=int(input())
    res=[]
    a=1
    while n:
        r=n%10
        if r!=0:
            res.append(r*a)
        a*=10
        n//=10
    print(len(res))
    print(*res)
            
        
        
    
