#06-dars: Sonlar

#a = 20
#b = 5.5
#temp = 36.6
#print(type(a))
#aholi_sone = 7_594_376_567
#print ("Aholisi soni:", aholi_sone)
#a, b, c = 10, 5.5, -56

#c = a*b
#print(c)

#d = 100/2
#print(d)

#radius = 20
#PI = 3.14159
#diametr = 2*radius
#print("Aylana uzunligi = ", PI*diametr)

#ism = "Jobir"
#yosh = 36
#yosh = str(yosh) #str ichiga bergan qiymatni matn tariqasida qaytaradi
#xabar = ism + " " +str(yosh)+ " yoshda"
#print(xabar)

#t_yil = int(input("Tug'ilgan yilingizni kiriting : "))
#yosh = 2023 - t_yil
#print("Siz ", yosh , " yoshda ekansiz !")

#a = int("10")
#b = float("10")
#temp = str(36.6)

#a = 20
#b = -30
#c = a + b
#print(c)

kvadrat_tomoni = 20
kvadrat_yuzi = kvadrat_tomoni**2
print("Kvadratning yuzi =  ", kvadrat_yuzi)

#pi = 3.14159 #float = o'nlik son
#radius = 10  #integer = butun
#print("Aylananing uzunligi ", pi * 2 * radius, " ga teng")

#aholi_soni = 7_594_000_000
#print("Yer kurrasida ", aholi_soni , " ga teng")

#Constant tushunchais yoq Pythonda
#PI = 3.14159 #Programmes just name it with capital letters
#radius = 21.2 #This is not a constant

#x, y, z = 10, -7.25, -30
#Birdaniga bir nechta o'zgaruvchiga qiymat berish uchun o'zgaruvchilar va ularga mos qiymatlar vergul (,) bilan ajrtailadi:

#ism = 'jobir'
#yosh = 36
#xabar = ism+ " " +str(yosh) + " yoshda"
#print(xabar)

#Typecasting str()-int yoki float turidagi sonlarni matnga o'zgartiradi
#int() - matn yoki float ko'rinishadi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerek.
#float() - matn yoki int ko'rinishadi qiymatlarni o'nlik songa o'zgartiradi.
#str(yosh) kodi yosh degan o'zgaruvchining qiymatini matn ko'rinishida ko'rsatdi xolos. Asl o'zgaruvchining qiymati sonligicha qoladi.. int() va float() ham huddi shunday ishlaydi.
#ism = "Jobir"
#yosh = 36
#print(type(ism))  #Ism degan o'zgaruvchining turini konsolga chiqaramiz
#print(type(yosh)) #Yosh degan o'zgaruvchining turini konsolga chiqaramiz
#t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#t_yil = int(t_yil)
#yosh = 2023 - t_yil
#print("Siz " +str(yosh) +  " da ekansiz !")
#son = int(input("Istalgan son kiriting: "))
#kvadrati = pow(son,3)
#print(kvadrati)

yosh = int(input("Sizning yoshingiz nechida ? "))
t_yil = 2023 - yosh
print("Siz " +str(t_yil)+ " da tug'ilgansiz")

bir = float(input("Birinchi sonni kiriting : "))
ikki = float(input("Ikkinchi sonni kiriting : "))
yigindi = bir + ikki
ayirma = bir - ikki
kopaytma = bir * ikki
bolinma = bir / ikki
print(yigindi, ayirma, kopaytma, bolinma)
print(bir,"+", ikki, "=", yigindi)
far = "farhod"
print("Mening ismim " +far)