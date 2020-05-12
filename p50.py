t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c,d=0,0
    a.sort(reverse=True)
    b.sort(reverse=True)
    for i in range(n):
        while d<n:
            
       
            if (a[i]>b[d]):
                c+=1
                d+=1
                break
            else:
                d+=1
    print(c)            
        
  
