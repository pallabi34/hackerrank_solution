t=int(input())
while t>0:
    t=t-1
    n=int(input())
    a=list(map(int,input().split()))
    c=[]
    for i in range(n):
        c.append(a.count(a[i]))
    m=max(c)
    r=n-m
    print(r)
    
