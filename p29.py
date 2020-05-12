t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for i in range(n):
        s+=l[i]
    print(s%k)
