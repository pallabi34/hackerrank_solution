import math
from decimal import*
i,j,k=map(int,input().split())
c=0
for l in range(i,j+1):
    n=(str(l)[::-1])
    if(abs(l-int(n))%k==0):
        c+=1
print(c)        
