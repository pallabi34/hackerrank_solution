t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    xi,yi=abs(x-z),abs(y-z)

    if(xi==yi):
        print("Mouse C")
    else:
        print("Cat A" if yi>xi else "Cat B")
