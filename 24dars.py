# 24-dars.Funksiyalar.So'ngSo'z

#lambda nomsiz funksiyalar yaratish

import math

uzunlik = lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))

kvadrat = lambda x,y:x**y
print(kvadrat(3,4))
#Example 2 funksiya yaash

def daraja(n):
    return lambda x:x**n
kvadrat = daraja(2)
print(kvadrat(2))
kub = daraja(3)
print(f"Kvadrati {kvadrat(2)} ga teng")

#Example 3
from math import sqrt
sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar))
print(ildizlar)

#Example 4
def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya!!!"""
    return x*x
sonlar = list(range(11))
print(list(map(daraja2,sonlar)))

#Example 5
sonlar1 = list(range(12))
kvadratlar=list(map(lambda x:x*x,sonlar))
print(kvadratlar)

#Example 6
a=[4,5,6]
b=[19,20,28]
a_plus_b = list(map(lambda x,y:x-y,a,b))
print(a_plus_b)

#Example 7
import random as r
sonlar = r.sample(range(100),10)
print(sonlar)

#Example 8
def justmi(x):
    """X juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return x%2==0
k = justmi(2)
just_sonlar=list(filter(justmi,sonlar))
print(just_sonlar)

#Example 9
just_sonlar=list(filter(lambda son:son%2==0,sonlar))
print(just_sonlar)

#Example 10
mevalar = ["olma","anor","anjir","shaftoli","o'rik","tarvuz","qovun","banana"]
harf = 'b'
mevavar_b=list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevavar_b)

#HomeWork = Fun time 

#Hw1
son1=lambda x:x*10
print(son1(10))

#Hw2
son2=lambda x,y:x**y
print(son2(2,3))

#Hw3
from random import sample
from math import sqrt

li=list(range(1001))
yes=sample(li,10)
print(yes)

ildizlar1=list(map(lambda n:sqrt(n),yes))
print(ildizlar1)

toq_sonlar = list(filter(lambda z:z%2==0,yes))
print(toq_sonlar)

#Hw4
def tubmi(x):
    if x%2==0 or x<2:
        return False
    if x==2 or x==3:
        return True
    for i in range(3,x,2):
        if x%i==0:
            return False
    return True
tub_sonlar=list(filter(tubmi,range(100)))
print(tub_sonlar)     
