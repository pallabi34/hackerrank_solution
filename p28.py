t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort()
    l=[]
    s=0
    for i in range(len(a)):
        l.append(min(a[i],b[i]))
    for j in range(len(l)):
        s+=l[j]
    print(s)    
