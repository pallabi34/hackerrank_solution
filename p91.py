def minSwaps(ar): 
    
      
    
    p = [*enumerate(ar)] 
      
    
    p.sort(key = lambda it:it[1]) 
      
    
    v = {k:False for k in range(m)} 
      
    
    ans = 0
    for i in range(m): 
          
        
        if v[i] or p[i][0] == i: 
            continue
              
       
        c = 0
        j = i 
        while not v[j]: 
              
            
            v[j] = True
              
            
            j = p[j][0] 
            c+= 1
              
       
        if c > 0: 
            ans += (c - 1) 
    
    return ans 
  
# Driver Code
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    ar=list(map(int,input().split())) 
    print(minSwaps(ar)) 
