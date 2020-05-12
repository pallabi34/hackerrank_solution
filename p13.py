t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    r=0
    c=0
    for i in range(n):
        a[i]+=r
        if(a[i]>=k):
            r=a[i]-k
            c+=1
        if(a[i]<k):
            break
    if(c==n):
        print("YES")
    else:
        print("NO",i+1)
            
