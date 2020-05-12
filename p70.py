m=1000000007
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    d=l[0]
    for i in range(1,n):
        l[i]=max(0,l[i]-i)
        d+=l[i]
    print(d%m)     
        
