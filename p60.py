T=int(input())
for i in range(T):
    a,b=map(int,input().split())
    w=int(a)+int(b)
    l1=len(str(w))
    l2=len(b)
    if(l1==l2):
        print(int(b))
    else:
        print(int(a)+int(b))
