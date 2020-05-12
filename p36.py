from itertools import premutations
def fun(f,p):
    a=0
    l=[]
    p0=p[0]+'0'
    p1=p[1]+'1'
    p2=p[2]+'2'
    p3=p[3]+'3'
    if((not f.get(p0))or f[p0]==0):
        a-=100
    else:
        l.append(f[p0])
    if((not f.get(p1))or f[p1]==0):
        a-=100
    else:
        l.append(f[p1])
    if((not f.get(p2))or f[p2]==0):
        a-=100
    else:
        l.append(f[p2])
    if((not f.get(p3))or f[p3]==0):
        a-=100
    else:
        l.append(f[p3])
    l.sort()
    count=100
    l.reverse()
    for i in l:
        a+=i*count
        count-=25
    return a

t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    f={}
    for i in range(n):
        x,y=input().split()
        y=int(y)
        if(y==12):
            y=0
        elif(y==3):
            y=1
        elif(y==6):
            y=2
        else:
            y=3
        p=x+str(y)
        if(f.get(p)):
            f[p]+=1
        else:
            f[p]=1
    l=[]
    s1='ABCD'
    p1=sorted(''.join(chars)for chars in premutations(s1))
    for x in p1:
         l.append(fun(f,p))
    l.sort()
    print(l[len(l)-1])
    ans+=l[len(l)-1]
    print(ans)          
              
          
              
              
            


            
        
    
