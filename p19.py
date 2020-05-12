t=int(input())
for _ in range(t):
    a=[]
    for i in range(3):
        b=input()
        a.append(b)
        c=0
    for i in range(2):
        for j in range(2):
            if a[i][j]=='l' and a[i+1][j]=='l' and a[i+1][j+1]=='l':
                c+=1
                break
    if c!=0:
        print("yes")
    else:
        print("no")
