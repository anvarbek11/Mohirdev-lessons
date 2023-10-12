#11-dars if-elif-else. Bir nechta shartlarni tekshirish
# Web sahifa : https://python.sariq.dev

#Example 1
#yosh = int(input("yoshingiz nechida? "))
#if yosh<=4:
#    narx = 0
#elif yosh <=12:
#    narx = 8000
#else:
#    narx = 10000
#print(f"Sizga kirish {narx} so'm")

#Example 2

#kun = input("Bugun nima kun?>>>")
#if kun.lower() == "shanba" or kun.lower() == "yakshanba":
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni ")

#Homework the fun part

#yosh = int(input("Sizning yoshingiz neccida >>> "))
#if yosh <= 4:
#    price = 0
#elif yosh<=12:
#    price = 5000
#elif yosh<65:
#    price = 10000
#else:
#    price = 8000
#print(f"Sizga kirish {price}")
#Example 3
#kun = input("Bugun nima kun >>>")
#harorat = float(input("Havo harorati qanday>>>"))

#if (kun.lower() == "yakshanba" or kun.lower()=="shanba") and harorat > 30:
#    print("Cho'milganni kettik !!!")

#elif kun.lower() == "yakshanba" and harorat<=30:
#    print("Bugun sovuq ekan")

#Example 4
#narx = 15000
#choy = True
#non = False

#if choy and non :
#    narx = narx +5000
#elif choy or non :
#   narx= narx +15000
#print(f"Jami narx: {narx}")

#Example 5 "in" operatori
#menu = ["osh", "qazonkabob","shashlik", "norin","somsa"]
#ovqat = input("nima ovqat yeysiz ?>>>")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi.")
#else:
#    print("Afsuski bizdab unday ovqat yoq ")

#Example 6
#menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = []
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
#else:
#   print("Buyerda unday ovqat yoq")

#if - elif - else zanjirining kamchiligidan biri, shartlardan biri bajarilishi bilan , qolgan shartlar tekshirilmaydi.

#narh = 15000
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#if choy:
#    print("Mijoz choy oldi: ")
#    narh = narh + 3000
#if salat:
#    print("Mijoz salat oldi:")
#    narh = narh + 5000
#if non:
#    print("Mijoz non oldi::")
#    narh = narh + 2000
#if kompot:
#    print("Mijoz kompot oldi: ")
#    narh = narh + 5000
#if assorti:
##    print("Mijoz assorti oldi:: ")
#    narh = narh + 15000
#print(f"Jami {narh} ga teng")

#menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#ovqat = input("Nima ovqat yeysiz>>>")
#if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi ! ")
#else:
#    print("Afsuski bu yerda bunday ovqat mavjud emas ! ")

#menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = ["osh","somsa","manti","shashlik"]
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"{taom} bu ovqat menuda bor")
#    else:
#        print(f"Kechirasi bu {taom} menuda yoq")

#menu = ["osh", "qazonkabob", "shashlik", "norin", "somsa"]
#buyurtmalar = ["osh","somsa","manti","shashlik"]
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"{taom} bu ovqat menuda bor")
#        else:
#            print(f"Kechirasi bu {taom} menuda yoq")
#else:
#    print("Savatchangiz bo'sh !!!")
#example 1:
#juft_son = int(input("Juft son kiriting: "))
#if juft_son % 2 == 0:
#    print("Rahmat!")
#else:
#    print("Bu son juft emas")
#example 2:
#yosh = int(input("Yoshingiz neccida>>> "))
#if yosh<4 or yosh>60:
#    narh = 0
#elif yosh<18:
#    narh = 10000
#elif yosh>18:
#    narh = 20000
#print(f"Kirish narxi {narh}")
#example 3:
#bir = float(input("Birinchi sonni kiriting: "))
#ikki = float(input("Ikkinchi sonni kiriting: "))
#if bir>ikki:
#    print(f"{bir} > {ikki}")
#elif bir<ikki:
#   print(f"{bir} < {ikki}")
#elif bir == ikki:
#    print(f"{bir} = {ikki}")

#Example - 4
#mahsulotlar = ["anor","uzum","olma","tarvuz","shaftoli","banan","qovun","pomidor","ananas","kiwi"]
#savat = []
#bor_mahsulotlar = []
#mavjud_emas = []
#for n in range(5):
#    savat.append(input(print(f"{n+1}-ni mahsulot nomini kiritng>>> ")))
#if savat:
#    for mahsulot in savat:
#        if mahsulot in mahsulotlar:
#            bor_mahsulotlar.append(mahsulot)
#        else:
#            mavjud_emas.append(mahsulot)
#else:
#    print("Savat bo'sh")
#print(f"Do'konimizda quyidagi mahsulotlar bor {bor_mahsulotlar}")
#print(f"Dokonimizda quyidagi mahsulotlar yo'q{mavjud_emas}")

#Example -5
#foydalanuvchilar = ["Anvar", "Sarvar","Javohir","Sobir","Toyir"]
#yangi_login = input("Yangi login tanlang: ")
#if yangi_login in foydalanuvchilar:
#    print("Login band, yangi login tanlang!")
#else:
#    print("Xush kelibsiz?")

#Example - 6
#butun = int(input("Istalgan butun son kiriting: "))
#for n in range(2,11):
#    if butun%n == 0:
#        print(f"{butun} soni {n} ga qoldiqsiz bo'linadi")

