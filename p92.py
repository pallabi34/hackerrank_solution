t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    li=[1]
    for i in range(1,n):
        if(l[i]-l[i-1]<=2):
            a=li.pop()
            li.append(a+1)
        else:
            li.append(1)
    print(min(li),max(li))        
            
            
        
