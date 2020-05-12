n=int(input())
l=[]
for i in range(n):
    li=int(input())
    l.append(li)
l.sort()
fi=[int(i) for i in l]
fii=sorted(fi)
for j in fii:
    print(j)
