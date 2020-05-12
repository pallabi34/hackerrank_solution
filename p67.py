def dis(n,l):
    flag=0
    c=[]
    for i in range(n):
        if(l[i]==1):
            c.append(i)
    for j in range(1,len(c)):
        if c[j]-c[j-1]<6:
            return ("NO")
            flag=1
            break
    if flag==0:
        return ("YES")
        

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(dis(n,l))
