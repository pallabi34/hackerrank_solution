n=int(input())
a=list(map(int,input().split()))
m=0
d=1
for c in a:
    n1=a.count(c)
    n2=a.count(c-d)
    m=max(m,n+n2)
print(m)    
