t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=list(s.strip())
    x,y=0,0
    for i in range(n):
        if(l[i]=="L"):
            x,y=(x-1),y
        elif(l[i]=="R"):
            x,y=(x+1),y
        elif(l[i]=="U"):
            x,y=x,(y+1)
        elif(l[i]=="D"):
            x,y=x,(y-1)
    print(x,y)        
             
