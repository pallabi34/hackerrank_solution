n=int(input())
p=[int(x) for x in str(n)]
odd=[p for i in p if p!=0]
even=[p for i in p if p==0]
for num in odd:
    if num==9:
        odd=1
    else:
        odd=num+2

print(odd)        
        
