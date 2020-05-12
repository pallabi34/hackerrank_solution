t=int(input())
for _ in range(t):
    n,a=map(int,input().split())
    ar=list(map(int,input().split()))
    q=list(map(int,input().split()))
    for i in range(a):
        for j in range(ar[q[i]]):
            c=max(ar)
            print(c)
        
        
