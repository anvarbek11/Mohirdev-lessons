#16-dars: Nesting

car1 = {
    'model':'lacetti',
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
}
car2 = {
    'model':'nexia',
    'rang':'qora',
    'yil':2015,
    'narh':9000,
    'km':89000,
    'korobka':'mexanika'
}
car3 = {
    'model':'gentra',
    'rang':'qizil',
    'yil':2019,
    'narh':15000,
    'km':20000,
    'korobka':'mexanika'
}
#cars = [car1,car2,car3]
#print(f"{cars[1]['model'].title()}"
#      f"{cars[1]['rang']}")
#for car in cars:
#    print(f"{car['model'].title()},"
#         f"{car['rang']} rang,"
#         f"{car['yil']},{car['narh']}$")
#malibus = []
#for n in range(10):
#    new_car = {
#        'model': 'malibu',
#        'rang': None,
#        'yil': 2020,
#        'narh': None,
#        'km': 0,
#        'korobka': 'avto'
#    }
#   malibus.append(new_car)

#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
#for malibu in malibus:
#    print(malibu)

#for malibu in malibus[6:]:
#    malibu['rang'] = 'qora'
#    malibu['korobka']='mexanika'
#    print(malibu)

#dasturchilar = {
#    'ali':['python','c++'],
#    'vali':['html','css','js'],
#    'hasan':['php','sql'],
#    'husan':['python','php'],
#    'maryam':['c++','c#']
#}
#for ism,tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
#    for til in tillar:
#        print(til.upper())


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']},

    'vali':{'familiya':'aliyev',
           'tyil':2001,
           'malumot':'orta maxsus',
           'tillar':['htm','css','js']},

    'hasan':{'familiya':'husanov',
           'tyil':1999,
           'malumot':'maxsus',
           'tillar':['python','php']}
}
#for ism,info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()},"
#          f"{info['tyil']} - yilda tug'ilgan. "
#          f"Ma'lumoti: {info['malumot']}\n"
#          "Quyidagi dasturlash tillarini biladi: ")
#    for til in info['tillar']:
#        print(til.upper())
#Homework part

#homewrok1
shaxs1 = {
    'ism':'Abu abdulloh muhammad ibn isroil',
    'tyil':818,
    'adress':'Buxoro',
    'umri':'60'
}
shaxs2 = {
    'ism':'Abdulla Qodiriy',
    'tyil':1894,
    'adress':'Toshkent',
    'umri':'44'
}
shaxs3 = {
    'ism':'Erking Vohidov',
    'tyil':1936,
    'adress':'Fargonada',
    'umri':'80'
}
shaxs4 = {
    'ism':'Alisher Navoiy',
    'tyil':1441,
    'adress':'Xirotda',
    'umri':'60'
}
shaxslar = [shaxs1,shaxs2,shaxs3,shaxs4]
#for shaxs in shaxslar:
#    print(f"{shaxs['ism']}"
#          f"{shaxs['tyil']}-yilda"
#          f"{shaxs['adress']}da tavallud topgan"
#          f"{shaxs['umri']} yil umr ko'rgan")

#for shaxs in shaxslar:
#    print(f"{shaxs['ism']} ning mashxur asarlari:")
#    if shaxs==shaxs1:
#        shaxs['asar'] = 'kecha', 'kunduz'
#        print(f"{shaxs['asar']}")
#    if shaxs==shaxs2:
#        shaxs['asar'] = 'qorongu', 'tunda'
#        print(f"{shaxs['asar']}")
#    if shaxs==shaxs3:
#        shaxs['asar'] = 'tundan', 'tonggacha'
#        print(f"{shaxs['asar']}")
#    if shaxs==shaxs4:
#        shaxs['asar'] = 'yes', 'no'
#        print(f"{shaxs['asar']}")
# Homewrok - 3
#kinolar = {
#   'Ali':['Teminator','Rambo','Titanic'],
#    'Vali':['Tenet','Inception','Interstellar'],
#    'Hasan':['Abdullajon','Bomba','Shaytanat'],
#    'Husan':['Mahallada duv-duv gap','John Wick']
#}
#for ism, kino in kinolar.items():
#    print(f"{ism.title()}ning sevimli kinolari: ")
#    for ki in kino:
#        print(ki.upper())

davlatlar = {
    'Ozbekiston':{'poytaxt':'Toshkent',
                  'hududi':448978,
                  'aholisi':33000000,
                  'pub birligi':'som'},
    'Rossiya': {'poytaxt':'Moskva',
                   'hududi': 17098246,
                   'aholisi': 144000000,
                   'pub birligi': 'rubl'},
    'AQSH': {'poytaxt':'Washington',
                    'hududi': 9631418,
                   'aholisi': 327000000,
                   'pub birligi': 'dollor'},
    'Malayziya': { 'poytaxt':'Kuala-Lumput',
                   'hududi': 329750,
                   'aholisi': 250000000,
                   'pub birligi': 'ringgit'}
}
davlat=input("Davlar nomini kiriting: ")
for nomi,nomlari in davlatlar.items():
    if nomi==davlat:
        print(f"{nomi}ning poytaxti {nomlari['poytaxt'].title()}")
        for n, k in nomlari.items():
            print(f"{n}: {k}")
    else:
        print("Bizda bu davlar haqida ma'lumot mavjud emas")








