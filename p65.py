t=int(input())
for _ in range(t):
    n=int(input())
    ar=list(map(int,input().split()))
    for i in range(len(ar)):
        ar[i]=ar[i]-i
    if(sum(ar)==1 or sum(ar)<=0):
        print(1)
    else:
        print(sum(ar))

    
       

