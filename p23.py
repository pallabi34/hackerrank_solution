t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]==a[j]):
                c=1
    if(c==1):
        print("yes")
    else:
        print("no")
                
                
