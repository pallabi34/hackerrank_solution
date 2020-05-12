t=int(input())
for i in range(t):
    a=input()
    ans=""
    c=1
    for j in range(1,len(a)):
        if(a[j]==a[j-1]):
            c+=1
        else:
            ans+=a[j-1]+str(c)
            c=1
    ans+=a[len(a)-1]+str(c)
    if len(ans)>len(a):
        print("NO")
    else:
        print("YES")
         
