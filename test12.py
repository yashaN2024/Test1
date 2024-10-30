#import pandas as pd
list54 = [134,152,522,5213]
#
# d = {0: "toyota","car": "5422345", 4: "geely"}
# # print(d["car"])
# # d["car2"] = "sfgsgd"
# # d.pop("car2")
# # print(d)
# # print(d.keys())
# # print(d.values())

#for keys, value in d.items


keys = (1,2,3,4,5,6,7,8)
#print(min(c))
values = ['a','b','c','d','e','f','g','h']
keys = [1,2,53,34,5,36,7,38, 38, 53]

# регулярные выражения
import re

s= input("введите логин")

pattern = r'\d'
st = re.sub(pattern,   "000" ,s)
print(st)
if not st:
    print("логин верный: ", s)

# найти наибольшее число в массиве, яв

num = []
s = input().split(" ")
max_square = 0
for i in range(int(s[0]), int(s[1])):
    sqrt = int(i ** 0.5)
    #print(sqrt*sqrt)
    if i == sqrt * sqrt:
        num.append(i)














