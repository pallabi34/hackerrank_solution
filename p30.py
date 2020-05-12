a=list(map(int,input().split()))
b=list(map(int,input().split()))
al=0
bo=0
l=[]
for i in range(len(a)):
    if a[i]>b[i]:
        al+=1
    elif a[i]==b[i]:
        ai=0
        bi=0
    else:
        bo+=1
print(al,bo)        
    
   
