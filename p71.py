import math as mt 
  
# Prints k factors of n if n can be written 
# as multiple of k numbers. Else prints -1 
def kFactors(n, k): 
      
    # list to store all prime factors of n 
    a = list() 
      
    for i in range(1,9999999999):
        while i % 2 == 0:
             a.append(2) 
             i = i // 2
             
    for j in range(3, mt.ceil(mt.sqrt(n)), 2): 
        while i % j == 0: 
            i = i / j; 
            a.append(j) 
              
    # This is to handle when n>2 and 
    # n is prime 
    if i > 2: 
        a.append(i) 
          
    # if size(a)<k,k factors are not possible 
    if len(a) < k: 
        print("-1") 
        return
          
    # printing first k-1 factors 
    #for i in range(k - 1): 
       # print(a[i], end = ", ") 
      
    # calculating and printing product  
    # of rest of numbers 
    product = 1
      
    for l in range(k - 1, len(a)): 
        product *= a[l] 
        c+=1
    if c==n and k>=2:
        print(1)
        return
        
  
# Driver code 
n, k = 4, 2
kFactors(n, k) 
