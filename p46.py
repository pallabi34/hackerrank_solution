def panagram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string=input()
if(panagram(string)==True):
    print("pangram")
else:
    print("not pangram")
