t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    count=0
    c=(a-b)
    if(c!=0):
       for i in range(1,c+1):
           if c%i==0:
               count+=1
               print(count)
    else:
         print(-1)
         
          
        
               
           
           
