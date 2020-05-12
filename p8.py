for _ in range(int(input())):
    scores=[0]*8
    for sub in range(int(input())):
        p,s=map(int,input().split())
        if p<=8:
            scores[p-1]=max(scores[p-1],s)
    print(sum(scores))       
