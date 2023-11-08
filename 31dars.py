#Example #1
from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomabilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        self.__km=km
        self.__id=uuid4()
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km +=km
        else:
            print("Mashinaning km ni kamaytirib bolmaydi")    
        
avto1=Avto("GM","Malibu","Qora",2020,4000,100000)
print(avto1.narh)
print(avto1.get_km())
print(avto1.get_id())
avto1.add_km(1500)
print(avto1.get_km())

#Example #2
class Avto:
    """Avtomobil klassi"""
    num_avto=0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto += 1
avto1 = Avto("GM","Malibu","Qora",2020,40000) 
avto2=  Avto("GM","Lacetti","Oq",2020,20000)
print(avto1.num_avto)  
avto3= Avto("Toyota","Carolla","Silver",2018,45000)
print(Avto.num_avto)

#Exampl 3
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.get_num_avto())        
#classmethod bu maxsus dekorator.Dekoratorlar bu o'z ichiga funksiya oluvchi funksiyalar. Dekoratorlar haqida keyingi darslarimizning birida batafsil to'xtalamiz.
#from odamlar import Talaba
#from transport import Avto
#talaba = Talaba("Alijon","Valiyev","FA010101","N000022")
#avto = Avto("GM","Malibu","Qora",2020,40000)
#Moduldan bitta klass import qilish uchun from modul import klass ifodasidan foydalanamiz;
#Bir nechta klasslarni import qilish : Moduldan bir nechta klass chaqirish talab qilinsa, import so'zidan so'ng klasslar ketma-kt vergul bilan ajratib yoziladi:    
#from odamlar import Talab,Shaxs
#talaba = Talaba ("Alijon","Valiye") 
#shaxs = Shaxs("Hasan","Husanovich")
#Modulni o'zini chaqirish#
#import odamlar 
#talaba = odamlar.Talaba("Alijon")    
#shaxs = odamlar.Shaxs("Hasan","Husanov","FB0011223")
#Moduldan barcha klasslarni import qilish
#Moduldagi barcha klasslar from odamlar import*
