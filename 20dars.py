#20-dars:Funksiyadan qiymat qaytarish

def toliq_ism_yasa(ism,familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
talaba = toliq_ism_yasa("Anvar","Kuziboev")
print(talaba)

#Example 2 
def toliq_ism_yasa(ism,familiya,otasining_ismi = ''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
yes=toliq_ism_yasa("Anvar","Kuziboev","Odilbekovich") 
print(f"Darsga kelmagan talabalar: {yes}")  

#Example 3
def avto_info(kompaniya,model,rangi,korobka,yili,narxi = None):
    avto = {"kompaniya":kompaniya,
            "model":model,
            "rang":rangi,
            "korobka":korobka,
            "yil":yili,
            "narx":narxi}
    return avto
yes1=avto_info('GM','Gentra','black','avtomat','2023','25000$')
yes2=avto_info('GM','Malibu','yellow','avtomat','2023')
avtolar = [yes1,yes2]
for k in avtolar:
    if k['narx']:
        narx = k['narx']
    else:
        narx = 'Nomalum'
    print (f"{k['rang']} {k['model']}. Narhi: {narx}")   

#Example 4
def oraliq(min,max):
    sonlar = []
    while min<max:
        sonlar.append(min)
        min+=1
    return sonlar
sonl=oraliq(0,10)
print(sonl)
#Example 5
def oraliq1(min,max,qadam=1):
    raqamlar = []
    while min<max:
            raqamlar.append(min)
            min += qadam
    return raqamlar
son=oraliq1(0,10,2)
print(son)  

#Homework Time

#Hw1
def lugat():
    lugatlar = {
        "Ismi":ism,
        'Familiya':familiya,
        'Tugilgan yili':t_yil,
        'Tugilgan joyi':t_joy,
        'Email address':email,
        'Telefon nomer':tel
    }
    return lugatlar
oh=('Anvarbek',"Kuziboev",1999,"Xorazm","anvarbek.kuziboev@gmail.com")
print(oh)

#Hw2
def lugat(Ismi,Familiya,Tugilgan,Tugilganj,emailaddress,Telefon):
    lugatlar = {
        "Ismi":ism,
        'Familiya':familiya,
        'Tugilgan yili':t_yil,
        'Tugilgan joyi':t_joy,
        'Email address':email,
        'Telefon nomer':tel
    }
    return lugatlar
print("lOl")
odamlar=[]
while True:
    ism=input("Ismingizni kiritn: ")
    familiya=input("Familiyangizni kiriting")
    t_yil=input("Tugilgan yilingizni kiring")
    t_joy=input("Tugilgan joyingizni kirint: ")
    email=input("Email addresingizni kiritin")
    tel=input("Telefon nomeringizni kiriitn:")
    odamlar.append(lugat(ism,familiya,t_yil,t_joy,email,tel))
    k=input("Davom etsangiz yes/no")
    if k =='no':
        break
print("Odamlar malumotlari : ")
for odam in odamlar:
    print(f"{odam['Ismi']}")    




#Hw3
def eng_kattasi(son1,son2,son3):
    print("3 ta son kiriting")
    if son1>son2 and son1>son3:
        return son1
    res=son1
    if son2>son1 and son2>son3:
        return son2
    res=son2
    if son3>son1 and son3>son2:
        return son3
    res=son3
    return res
yes = eng_kattasi(5,6,7) 
print(f"Sonlarning eng kattasi bu - {yes}")   

#Hw4
def aylana (radius):
   diametr=2*radius
   perimetr=2*3.14*radius
   yuzi = 3.14*(radius**2)
   lugat={
       "Radius":radius,
       "Diametri":diametr,
       "Perimetri":perimetr,
       "Yuzi":yuzi
   }
   return lugat
k = aylana(2)
print(k)

#Hw5
def tub_sonlar_top(min, max):
    tub_sonlar = []
    for n in range(min, max + 1):
        tub = True
        if n == 1:
            tub = False
        elif n == 2:
            tub = True
        else:
            for x in range(2, n):
                if n % x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)

    return tub_sonlar
yes=tub_sonlar_top(1,10)
print(yes)
#Hw6
def fibonacchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fibonacchi(10))        


        







    

    




