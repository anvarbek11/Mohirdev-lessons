#22dars-moslashuvchan funksiya(*args**kwargs)
#Example 1
def summa (*sonlar):
    """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(4,5,6,7))    
#Tuple -> O'zgarmas ro'yxat
#Example 2
def summa(*sonlar):
    """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
    return sum(sonlar)
print(summa(1,2))
#Example 3
def summa (x,y,*sonlar):
    """Kiritlgan sonlar yig'indisini qaytaradigan funksiay"""
    return x+y+sum(sonlar)
print(summa(1,2,3,4,5))
#Example 4
def avto_info(kompaniya,model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaradigan funksiya"""
    malumotlar['Kompaniya']=kompaniya
    malumotlar["Model"]=model
    return malumotlar
avto1=avto_info("GM","Cobalt",rang='qora',narx=19000,tezligi=200)
print(avto1)      

#Homework tima = Fun time 

#Hw1
def istalgancha(*raqamlar):
    """Istalgancha sonlar qabul qilib ularning ko'paytmasini qaytaruvchi funksiya"""
    kopaytma = 1
    for raqam in raqamlar:
        kopaytma = kopaytma*raqam
    return kopaytma
k = istalgancha(1,2,3,4,5)
print(k)    

#Hw2
def talabalar_haqida(ism,familiya,**ixtiyoriy):
    """Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    ixtiyoriy["Ism"]=ism
    ixtiyoriy["Familiya"]=familiya
    return ixtiyoriy
t1=talabalar_haqida('Anvar','Kuziboev',boyi=172,kilo=77,rangi='qora')
print(t1)
    

            
                
                
                
                


