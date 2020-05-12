a=list(map(int,input().split()))
min=0
max=0
n=len(a)
for i in range(n-1):
    min+=a[i]
for i in range(1,n):
    max+=a[i]
print(min,max)    
    
