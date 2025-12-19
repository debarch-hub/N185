# 4-masala. Sonlardan iborat tuple qabul qiladigan va tupledagi barcha juft sonlar yig’indisini chiqaruvchi rekursiv funksiya yozing
# Input: (2,3,5,6,3,7,8,4)
# Output: 20

import os
from re import T
os.system("clear")
def juft_yigindi(t, i=0):
    if i == len(t):
        return 0
    if t[i] % 2 == 0:
        return t[i] + juft_yigindi(t, i+1)
    else:
        return juft_yigindi(t, i+1)

t = (2,3,5,6,3,7,8,4)
print(juft_yigindi(t))
