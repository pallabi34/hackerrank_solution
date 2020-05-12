t=int(input())
for _ in range(t):
    n=int(input())
    l=0
    for i in range(n):
        p,q,d=map(int,input().split())
        a=p+((d/100)*p)
        b=((d/100)*a)
        c=a-b
        d=p-c
        e=d*q
        l+=e
    print(l)    
        
    
        
