t=int(input())
count=0
st=['ch','he','ef','che','hef','chef']
for i in range(t):
    s=input()
    for i in st:
         if(i in s):
            count+=1
            break
print(count)        
        
