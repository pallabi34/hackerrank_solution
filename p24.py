T=int(input())
for tc in range(T):
    N=int(input())
    a=[int(x) for x in input().split()]
    b=list([x for x in a if a.count(x) > 1])
    print(b)
