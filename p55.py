n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
for i in range(max(a),min(b)+1):
    for j in a:
        if i%j!=0:
            break
    else:
        for k in b:
            if k%i!=0:
                break
        else:
            c+=1
print(c)            
            
