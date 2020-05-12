def difference(arr,n):
    d1=0
    d2=0
    for i in range(n):
        d1+=arr[i][i]
        d2+=arr[i][n-i-1]
    return abs(d1-d2)
n=int(input())
arr=[x[:] for x in [[int(input())]*n]*n]
print(difference(arr,n))
