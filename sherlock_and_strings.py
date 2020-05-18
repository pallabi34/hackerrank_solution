import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the isValid function below.
def isValid(s):
    #s=len(s)
    ar=[0]*26
    for i in s:
        ar[ord(i)-97]+=1
    d=defaultdict(int)
    for i in ar:
        if i>0:
            d[i]+=1
    print(d)
    if len(d.keys())>2:
        return "NO"
    elif len(d.keys())==2:
        ar=list(d.keys())
        if abs(ar[0]-ar[1])==1:
            if d[ar[0]]==1 or d[ar[1]]==1:
                return "YES"
            else:
                return "NO"
        elif (ar[0]==1 and d[ar[0]]==1) or (ar[1]==1 and d[ar[1]]==1):
            return "YES"
        else:
            return "NO"



    else:
        return "YES"


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
