t=int(input())
for _ in range(t):
    f,d,t,b=map(int,input().split())
    t1=2*(f+d)/t
    t2=(f**2)/(b**2)
    if(t1<t2):
        print("Tiger")
    else:
        print("Bolt")
