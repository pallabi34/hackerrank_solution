t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    ph=0
    s=0
    for i in range(n):
        if h[i]-ph > k:
            s+=(h[i]-ph)//k
        ph=h[i]
    print(s)   
