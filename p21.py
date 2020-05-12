from collections import counter
t=int(input())
for _ in range(t):
    s=input()
    d=counter(s)
    l=[]
    for a in d:
        l.append(d[a])
    c=len(a)
    if c<3:
        print("Dynamic")
        continue
    else:
        l=sorted(l)
        flag=0
        if c>3 and l[3]==l[2]+l[0]:
            t=l[0]
            l[0]=l[1]
            l[1]=t
        for i in range(2,c):
            if l[i]==l[i-1]+l[i-2]:
                continue
            else:
                flag=1
                break
        if flag==0:
            print("Dynamic")
        else:
            print("Not")
            
        
        
    
















































































































              
    print(n-m)       
        
            

