
def trace(a, n):  
  
    sum = 0  
    for i in range(n):  
        sum += a[i][i] 
    return sum  

def countrows(a,n):
    count=0
    for i in range(n):
        row=set()
        for j in range(n):
            if a[i][j] in row:
                count+=1
                break
            else:
                row.add(arr[i][j])
    return count            
            
  
       





   
