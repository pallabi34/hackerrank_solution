n=int(input())
l=list(map(int,input().split()))
a=0
b=abs(l[0]-l[1])
for i in range(2,n):
    h1=a+abs(l[i]-l[i-2])
    h2=b+abs(l[i]-l[i-1])
    a=b
    b=min(h1,h2)
print(b)    
    
    
