r1=list(map(int,input().split()))
r2=list(map(int,input().split()))

if r1[2]>r2[2]:
    print(10000)
elif r1[2]<r2[2]:
    print(0)
elif r1[1]>r2[1]:
    print(500 * abs(r1[1]-r2[1]))
elif r1[1]<r2[1]:
    print(0)
elif r1[0]>r2[0]:
    print(15 * abs(r1[0]-r2[0]))
else:
    print(0)
    
