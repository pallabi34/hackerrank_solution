t=int(input())
for _ in range(t):
    rt=int(input())
    rt1=list(map(int,input().split()))
    rd=int(input())
    rd1=list(map(int,input().split()))
    st=int(input())
    st1=list(map(int,input().split()))
    sd=int(input())
    sd1=list(map(int,input().split()))
    truth=0
    dare=0
    for i in range(st):
        if(st1[i] in rt1):
            truth+=1
    for j in range(sd):
        if(sd1[j] in rd1):
            dare+=1
    if(truth==st) and(dare==sd):
        print("yes")
    else:
        print("no")
            
