t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    li=[]
    for i in range(1,n):
        li.append(l[i]-l[i-1])
    if(li.count(li[0])==len(li)):
        c=n
        d=n
    else:
        c=sum(map(lambda x:x>2,li))
        d=sum(map(lambda x:x<=2,li))
        c+=1
    print(c,d)    
