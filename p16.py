t=int(input())
while t>0:
    ar=[int(x) for x in input().split()]
    s=ar[0]
    ar=ar[1:]
    c=0
    sn=0
    n=len(ar)
    while n>0:
         item=ar.pop()
         n-=1
         sn+=item
         if sn>s:
             ar.append(item)
             c+=1
             n+=1
             sn=0
            
    print(c+1)
    t-=1
        
    
        
    

    
    
