t=int(input())
for _ in range(t):
    k=0
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    p=100-s
    for i in range(n):
        for j in range(i+1,n):
            if(b[i]!=b[j]):
                sum=a[i]+a[j]
                if(sum<=p):
                    k=1
                    break
                
                
    if(k==1):
        print("yes")
    else:
        print("no")
