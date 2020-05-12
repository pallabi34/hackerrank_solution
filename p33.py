t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    for i in range(1,n):
       for j in range(1,n):
           if i+j==k and i*j==k:
               print("YES")
           else:
               print("NO")
               
           
           
         
