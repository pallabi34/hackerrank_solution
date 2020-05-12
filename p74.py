
    n=int(input())
    a=list(map(int,input().split()))
    c=[]
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]-a[j]>=0):
                c.append(a[i]-a[j])
    print(min(c))            
            
            
