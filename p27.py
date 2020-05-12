t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    n1=len(a)
    n2=len(b)
    s=0
    for i in range(n1):
        for j in range(n2):
            p=min(i,j)
            s+=p
    print(s)        
