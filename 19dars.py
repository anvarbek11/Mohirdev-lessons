#19-dars:Functions (Funksiyalar)

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalamu aleykum!!!")
#salom_ber()   
#def salom_ber(ism):
#    """Foydalanuvchinig ismini qabul qilib, unga salom beruvchi funksiya"""
#    print(f"Asslamu alyekum, hurmatli {ism.title()}")
#salom_ber('hasan')
#salom_ber('olim')

#def yosh_hisoble(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")    
#yosh_hisoble('anvar',1999)

#def yosh_hisobla(tugilgan_yil, joriy_yil=2023):
#    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#yosh_hisobla(1999,2022)    

#amaliyot1 
def tug_yil(ism,yosh):
    """"Foydalanuvchining tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()}ning yoshi {2023-yosh} da")
tug_yil('Anvar',1999)  

#amaliyot2
def kvadrat_kub(son):
   
   """Foydalanuvchidan son olib uning kvadrati va kubini hisoblaydigan funksiya"""
   print(f"{son} ning kvadrati: {son**2} ga teng\n"
         f"{son} ning kubi {son**3} ga teng") 
kvadrat_kub(2)   
#amaliyot3
def juft_toq(son):
    """Sonning juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son%2==0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")
juft_toq(-5)            
#amaliyot4
def ikkita_katta_kichik(son1,son2):
    if son1>son2:
        print(f"{son1} eng kattasi")
    if son1<son2:
        print(f"{son2} eng kattasi")
    else:
        print("Sonlar teng")    
ikkita_katta_kichik(5,5)   
#amaliyot5
def x_y(x,y):
    "X ning y chi darajasini konsolga chiqaradigan funksiya!!!"
    p = pow(x,y)
    print(f"X ning Y chi darajasi = {p}")
x_y(2,3)  
#amaliyot6
def x_y_standard(x,y=2):
    """X ning y standard bolgandagi darajasini topish!!!"""
    z=pow(x,y)
    print(f"X ning 2 darajasi = {z}")
x_y_standard(2)   
#amaliyot7
def bolinish_amaliyotlari(son):
    """Bo'linish alomatlarini konsolga chiqaradigan funksiya!!!"""
    for i in range(2,10):
        if son%i==0:
            print(f"{son} {i} ga qoldiqsiz bo'linadi")
    
bolinish_amaliyotlari(70)                   


