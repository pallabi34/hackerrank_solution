t=int(input())
for _ in range(t):
    s=input()
    r=s[::-1]
    for i in range(1,len(s)):
        a=abs(ord(s[i])-ord(s[i-1]))
        b=abs(ord(r[i])-ord(r[i-1]))
        if(a!=b):
            print("Not Funny")
            break
        
    else:
         print("Funny")
            
            
            
        
            
        
