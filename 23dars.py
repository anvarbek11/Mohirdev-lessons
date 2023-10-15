#23-dars. Modul nima ?
#Example 1

import avto_info
avto1 = avto_info.avto_info1("Gm","Malibu","Qora",2020,4000)
avto_info.info_print(avto1)

#Example 2
import avto_info as aim
avto1=aim.avto_info1("LOL","Malibu","Qora",2023,5000)
aim.info_print(avto1)

#Example 3
from avto_info import avto_info1 as ainfo, info_print as iprint
avto1=ainfo("LOL","Malibu","Qora",2023,5000)
iprint(avto1)

#Example 4

import math
x=400
print(math.sqrt(x))
print(math.pow(5,3))
print(math.pi)
print(math.log2(8))
print(math.log10(100))

#Example 5
import random as r
son = r.randint(0,100)
print(son)

#Example 6
ismlar = ["olim", "anvar","hasan","husan"]
ism=r.choice(ismlar)
print(ism)
print(r.choice(ism))

#Example 7
x = list(range(0,51,5))
print(x)
print(r.choice(x))

#Example 8
x = list(range(11))
print(x)
r.shuffle(x)
print(x)

#Homework = Fun time 
