def trace(ar, n):  
  
    sum = 0  
    for i in range(n):  
        sum += ar[i][i] 
    return sum

def find_rows(ar,n):
    cnt=0
    for i in range (n):
        row=set()
        for j in range (n):
            if ar[i][j] in row:
                cnt+=1
                break
            else:
                row.add(ar[i][j])
    return cnt

def find_columns(ar,n):
    cnt=0
    for i in range (n):
        column=set()
        for j in range (n):
            if ar[j][i] in column:
                cnt+=1
                break
            else:
                column.add(ar[j][i])
    return cnt

case=int(input())
for case in range(1,case+1):
    n=int(input())
    ar=[] 
    for i in range(0,n):
        ar.append([int(j) for j in input().split()])
    trace1= trace(ar, n)
    find_rows1=find_rows(ar,n)
    find_columns1=find_columns(ar,n)
    print('Case #{}:{} {} {}'.format(case,trace1,find_rows1,find_columns1))
   

    

        
            
