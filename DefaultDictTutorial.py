from collections import defaultdict
from typing import DefaultDict

mA,mB = map(int, input().split())
d=defaultdict(list)
list1=[]
for i in range(1,mA+1):
    d[input()].append(str(i))
# for i in range(0,mB):
#     list1=list1+[input()]
for _ in range(mB):
    w = input()
    if(w in d):
        print(" ".join(d[w]))
    else:
        print(-1)