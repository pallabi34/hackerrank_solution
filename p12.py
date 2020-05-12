from itertools import combinations
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(combinations(l,k))
    l2=[]
    for j in l1:
        l2.append(sum(j))
    print(l2.count(min(l2)))    
