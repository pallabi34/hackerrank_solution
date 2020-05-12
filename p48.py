n=int(input())
p=[int(x) for x in str(n)]
for i in range(len(p)):
    if(p[i]%2==0 and p[i]!=8):
        p[i]+=2
    elif(p[i]%2!=0 and p[i]!=9):
        p[i]+=2
    elif(p[i]==8):
        p[i]=0
    elif(p[i]==9):
        p[i]=1
ne=[str(x)for x in p]
res=("".join(ne))
print(res)
