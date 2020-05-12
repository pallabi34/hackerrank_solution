def array(ar[],ar1[],s):
    ar[0]=0
    ar[1]=4
    p=5
    for i in range(2,400):
        ar[i]=p
        if((i%400==0)or (i%4==0 and i%100!=0)):
            p=(p+2)%7
        else:
            p=(p+1)%7
        
        for i in range(1,400):
            if((i%400==0) or (i%4==0 and i%100!=0)):
                if(ar[i]==6):
                    ar1[i-1]=1
                else:
                    ar1[i-1]=0
            else:
                 if(ar[i]==6 or ar[i]==0):
                   ar1[i-1]=1
                 else:
                     ar1[i-1]=0
                
                   
              
        for  x in ar1:
            s+=x


def solve(m1,y1,m2,y2):
    if(m1>2):
        y1+=1
    if(m2<2):
        y2-=1
    a=y1%400-1
    b=y2%400-1
    if(a==-1):
        a=399
    if(b==-1):
        b=399
    ans=0
    if((y1//400)==(y2//400)):
        for i in range(a,b):
            ans+=ar[i]
        print(ans)
    else:
        d=(y2//400)-(y1//400)
        ans+=(d-1)*s
        for i in range(a,400):
            ans+=ar1[i]
        for i in range(0,b):
            ans+=ar[i]
        print(ans)

t=int(input())
ar=[]
ar1=[]
s=0
array(ar[],ar1[],s)
for _ in range(t):
    m1,y1=map(int,input().split())
    m2,y2=map(int,input().split())
    solve(m1,y1,m2,y2)
        
                
        
