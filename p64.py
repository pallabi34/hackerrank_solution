n=int(input())
a=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if(arr[i]==n):
        print(i)
