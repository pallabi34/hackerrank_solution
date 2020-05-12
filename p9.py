t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in arr:
        x=arr.count(i)
        if(x>c):
            c=x
    print(n-c)
