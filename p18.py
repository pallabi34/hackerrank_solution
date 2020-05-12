t=int(input())
for _ in range(t):
    a=int(input())
    b=list(input())
    c=list(input())
    i=0
    m=0
    while i<a:
        if b[i]==c[i]:
            m+=1
            i+=1
        elif c[i]==N:
            i+=1
        else:
            i+=2
            
    print(m)        
