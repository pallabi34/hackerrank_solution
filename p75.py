t=int(input())
for _ in range(t):
    n=int(input())
    a=0
    b=0
    c=0
    if(n==0 and n==1 and n==2):
        print(0)
    else:
        while(n>2):
            a=(n-1)
            b+=1
            if(a==b):
                break
            elif(a!=b and a>b):
                c+=1
            n-=1    
    print(c)         
