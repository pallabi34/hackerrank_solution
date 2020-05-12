t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a[0][0]="W"
    for i in range(1,n):
        a[i][0]="B"
    for j in range(1,m):
        a[0][j]="B"
    for i in range(1,n):
        for j in range(1,m):
            a[i][j]="B"
    for i in range(1,n):
        for j in range(1,m):
            print(a[i][j],end=" ")
            
