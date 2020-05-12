t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    p=m+n
    a=list(map(int,str(p)))
    b=list(map(int,str(n)))
    if(len(a)==len(b)):
        print(n)
    else:
        print(m+n)
