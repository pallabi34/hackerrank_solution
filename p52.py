n=int(input())
l=list(map(int,input().split()))
p=9999999999
for i in range(n):
    for j in range(n):
        if(l[i]==l[j]) and (i!=j):
            p=min(p,abs(i-j))
if p==9999999999:
    p=-1
   
          
        
print(p)      
