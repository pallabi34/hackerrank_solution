n,k=map(int,input().split())
a=list(map(int,input().split()))
b=int(input())
bc=(sum(a)-a[k])//2
if(bc==b):
    print("Bon Appetit")
elif bc<b:
    print(b-bc)
