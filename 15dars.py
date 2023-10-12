#15-dars. Lug'at elementlari bilan ishlash

#items - elementlar

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
}
#for k,q in telefonlar.items():
#    print(f"{k.title()} ning telefon {q}")

#mahsulotlar = {
#   'olma':10000,
#    'anor':20000,
#    'uzum':40000,
#    'anjir':25000,
#    'shaftoli':30000
#}
#print("Do'kondagi mahsulotlar : ")
#for k in mahsulotlar.keys():
#    print(k.title())

#bozorlik = ['anor','uzum', 'non','baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#    else:
#        print(f"iltimos , dokoningizga {mahsulot} ham olib keling ")
#print("Do'konmizdagi mahsulotlar: ")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())
#print(mahsulotlar.keys())
#print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
#for tel in telefonlar.values(): #values take value from dictionary
#    print(tel)
#print(type(telefonlar))
#toys = {"ball", "car", "lamp", "ball","bear","car"}
#print(toys)

#print("Foydalanuvchilar quyidagi telefonlarni ishlatishgan: ")
#for tel in set(telefonlar.values()):
#    print(tel)

#Amaliyot :
#python = {"Boolean":"mantiqiy qiymat",
#          "Float":"O'nlik son",
#          "For":"Biror amalni qayta-qayta bajarish tsikli",
#          "If":"Shartlarni tekshirish operatori",
#          "Integer":"Butun son",
#          "else":"Aksincha",
#          "In":"ichida"}
#for k,v in sorted(python.items()):
#   print(f"{k}-{v}")

davlatlar = {'AQSH':'Washington D.C',
             "Italiya":"Rim",
             "Malayziya":"Singapur",
             "O'zbekistno":"Toshkent",
             "Qirg'iziston":"Bishkek",
             "Qozog'izton":"Nursulton",
             "Rossiy":"Moskva",
             "Singapur":"Kuala-lumpur",
             "Tojikiston":"Dushanbe"}
bosh=[]
bosh.append(input("Qaysi davlatning poytaxtini bilishni istaysiz? "))
for i in bosh:
    if i in davlatlar:
        print(f"{i.upper()}ning poytaxti {davlatlar[i]}")

#print("Dunyo davlatlari : ")
#for davlat in sorted(davlatlar.keys()):
#    print(f"{davlat.upper()}")
#print("Davlatlarning poytaxtlari: ")
#for poytaxt in sorted(davlatlar.values()):
#    print(f"{poytaxt.title()}")
#menu = {"osh":20000 ,
#        "non": 4000,
#        "qozonkabob":60000,
#        "shashlik":15000,
#        "somsa":10000,
#        "lagmon":35000}
#zakaz = []
#print("3 ta taom buyurtma bering.")
#for n in range(3):
#   zakaz.append(input(f"{n+1}-taom"))
#for ovqat in zakaz:
#    if ovqat in menu:
#        print(f"{ovqat.title()} {menu[ovqat]}")
#    else:
#        print(f"{ovqat} yo'q")







