import math
str=''
for i in range(int(input())):
    n,a,b=list(map(int,input().split()))
    for i in range(97,97+b):
        str+=chr(i)
    m=len(str)
    while(m<n):
        for i in range(b):
            str+=str[i]
            m=len(str)
            if(m==n):
                break
        if(m==n):
            break
    print(str)
    str=" "
    
