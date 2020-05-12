t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    p=[]
    r=''
    
    for i in range(len(l)):
        if l[i]%10==0:
            p.append(l[i])
            q=sum(p)
            break
        else:
            l[i]=(int(x) for x in str(l[i]))
            p.append(sum(l[i]))
            p.sort(reverse=True)
    for j in p:
       r+=str(j)
       q=r
print(q)       
