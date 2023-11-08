#32-dars Dunder metodlar
#Pythondagi maxsus metodlar bilan tanishamiz
#Dunder - double underscore yoki qisqa qilib dunder metodlar deb ataladi.
#Dunder metodlardan biz __init__ metodi bilan tanishdik. Bu metod klassdan obyekt yaratishda chaqiriladi va obyektning xususiyatlarini belgilaydi. 
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobil xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        Avto.__num_avto += 1
    def __repr__(self):
        """Obyekt haqida ma'lumot"""   
        return f"AVto:{self.rang} {self.model} {self.make}" 
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narh<=boshqa_avto.narh
#Obyektga print() yoki str() orqali murojat qilinganda obyekt haqida tushunarli ma'lumot qayatarish uchun __repr__ va __str__ metodlaridan foydalanamiz. Tushunarli bo'lishi uchun avvalgi darsimizdagi Avto klassiga qayatamiz
avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot   
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto1>avto2
#Example 2 Obyektlarni taqqoslash
x,y=5,10
print(x<y)

matn = "hello world"
print(len(matn))
sonlar = [12,34,56,66]
print(len(sonlar))

#Example 4
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name=name
        self.avtolar = []
    def __repr__(self):
        return f"{self.name} avtosaloni" 
    def add_avto(self,avto):
        if isinstance(avto,Avto):
            self.avtolar.append(avto) 
        else:
            print("Avto obyekitini kiriting")   
    def __len__(self):
        return len(self.avtolar) 
    def __getitem__(self,index):
        return self.avtolar[index]  
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value      
# Avto obyektlarini yaratamiz
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
salon1 = AvtoSalon("MaxAvto")
print(salon1)
# Yuqoridagi obyektlarni salon1 ga qo'shamiz
for avto in [avto1, avto2, avto3]: 
    salon1.add_avto(avto)
print(len(salon1))
3 # Salonimizda 3 ta moshina bor
print(salon1[0])
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
salon1[0]=avto4
print(salon1[0])