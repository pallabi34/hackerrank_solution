n=int(input())
l=list(map(int,input().split()))
p=0.0
ne=0.0
e=0.0
for num in l:
    if num>0:
        p+=1
    elif num==0:
        e+=1
    else:
        ne+=1
print(p/n)
print(ne/n)
print(e/n)
