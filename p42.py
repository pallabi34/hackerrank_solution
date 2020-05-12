t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    if n>=38:
        mod=n%5
        if mod>=3:
            n+=(5-mod)
    print(n)         
