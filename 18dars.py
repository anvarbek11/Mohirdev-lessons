#18-dars: While va ro'yxatlar

#print("Yaqin do'stlaringiz ro'yxatini tuzamiz: ")
#ismlar = []
#n=1
#while True:
#    savol=f"{n}-do'stingiz ismini kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("yana ism qo'shasizmi? (xa/yoq)")
#    n += 1
#    if takrorlash != 'xa':
#        break
#print("Do'stlaringiz royxati: ")
#for i in ismlar:
#    print (i)

#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Dostingiz ismini kiriting: ")
#    yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism]=int(yosh)
#    javob = input("yana ma'lumot qo'shasizmi? (xa/yoq)")
#    if javob=='yoq':
#        ishora=False
#for ism,yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")        


#cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
#while 'nexia' in cars:
#    cars.remove("nexia")
#print(cars)    


#talabalar = ["hasan", "husan","olim","botir"]
#baholangan={}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan[talaba]=int(baho)
#print(talabalar)
#print(baholangan)

#Homework time 
print("Buyurtma qabul qiluvchi dastur !!!!")
print("Buyurtmani tugatishni xohlasangi 'yoq' deb yozing ")
buyurtmalar = []
buyurtma = ("Nima buyurtma qilishini xohlaysiz: ")
while True:
    qiymat = input(buyurtma)
    if qiymat=="yoq":
        break
    buyurtmalar.append(qiymat)    
print(buyurtmalar)    

#2a
print("E-bozor uchun mahsulotlar va ularning narhlari lug'ati!!!")
lugat = {}
while True:
    mah = input("Mahsulot nomini kiriting>>>")
    narh= int(input("Mahsulot narxini kiriting>>>"))
    lugat[mah]=narh
    takrorlash = input("Yana mahsulot kiritishni xohlaysizmi (xa/yoq>>>)")
    if takrorlash=='yoq':
        break
for i,k in lugat.items():
    print(f"{i}:{k}")

#3
print("Ikkita lugatni solishtiramiz ")
for mahsulot in buyurtmalar:
    if mahsulot in lugat:
        print(f"Mahsulot narxi : {lugat[mahsulot]}")
        break
    else:
        print("bizda bunday mahsulot yoq")    


