t=int(input())
for _ in range(t):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(a):
        for j in range(i,a):
            if(b[i]%2==0 and b[j]%2!=0):
                c+=1
    print(c)            
