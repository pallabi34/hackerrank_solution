t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(input().split())
    r=a[:n-k]
    print(r.count('H'))

