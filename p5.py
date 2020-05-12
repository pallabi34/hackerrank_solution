t=int(input())
for i in range(t):
    n=int(input())
    m=list(map(int,input().split()))
    d=[]
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if(m[i]<m[j]):
                c+=1
        d.append(c)
    print(*d)    
