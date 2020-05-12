def minDist(arr, n, x, y): 
    min_dist = 99999999
    for i in range(n): 
        for j in range(i + 1, n): 
            if (x == arr[i] and y == arr[j] or
            y == arr[i] and x == arr[j])and min_dist > abs(i-j):   
                min_dist = abs(i-j) 
        if (min_dist>=6 and min_dist<99999999):
            return ("YES")
        else:
            return ("No")
        
  
  

for _ in range(int(input())):
    n = int(input())
    arr=list(map(int,input().split())) 
    x = 1
    y = 1
    print( 
     minDist(arr, n, x, y)) 
    
