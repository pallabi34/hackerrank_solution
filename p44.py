n=int(input())
a=list(map(int,input().split()))
maxi=0
diff=1                                                                               
for k in a:
    n1=a.count(k)
    n2=a.count(k-diff)
    print(n1,n2)
    
