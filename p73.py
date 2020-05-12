t=int(input())
for _ in range(t):
    m=int(input())
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]+a[j]==m):
                print(i+1,j+1)
