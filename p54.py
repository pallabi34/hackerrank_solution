s=input()
st=[]
for i in s:
    if not st:
        st.append(i)
    else:
        if st[-1]==i:
            st.pop()
        else:
            st.append(i)
if not st:
    print("Empty String")
else:
    print(''.join(st))
