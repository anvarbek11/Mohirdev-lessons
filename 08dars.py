#08-dars. Ro'yxatlar bilan ishlash

cars = ["bmw", "mercedes benz", "volvo", "general motors", "tesla", "audi"]
#cars.sort() #Ro'yxatni alifbo ketma-ketligida tahladi
#print(cars)
#cars.sort(reverse=True)
#print(cars)

#print(sorted(cars))
#print(sorted(cars, reverse=True))
#cars.reverse()
#print(cars)
#print(len(cars)) #Ro'yxatlarning uzunigini chiqarish uchun foydalanamiz!!!
#Range funksiyasi
#sonlar = [10,20,31,41,51,61]
#sonlar = list(range(0,11))
#print(sonlar)

#toq_sonlar = list(range(1,20,2))
#print(toq_sonlar)
#juft_sonlar = list(range(0,20,2))
#print((juft_sonlar))
#max_qiymat = max(toq_sonlar)
#max_juft = max(juft_sonlar)
#print(max_qiymat)
#print(juft_sonlar)

cars = ["mers", "bmw", "rolce royc", "general motors", "chevrolet"]
#print(cars[0:3])
#print(cars[2:7])
#print(cars[:3])
#print(cars[1:])
#my_cars = cars
#print(cars)
#my_cars.remove("bmw")
#print(my_cars)
#my_cars[0] = "Lacetti"
#print(my_cars)
#print(cars)
#print(cars)
#my_cars = cars[:] #Boshidan oxirigacha cars dagi hamma elementlarni olib my_cars ga joylab qo'y degan
#cars.remove("mers")
#print(cars)
#print(my_cars)

#Tuple o'zgarmas ro'yxat () shu qavslardan foydalanamiz
#toys = ("bus", "car", "bear", "dino", "snake", "lizard")
#toys = list(toys)
#toys = tuple(toys)
#toys.append("teddy")
#print(toys)

#Homework
#cars = ["mers","toyota", "bmw"]
#cars.sort(reverse=True)
#print(cars)

#Ro'yxatni aylantirish
#fruits = ["pera", "banana",'apple','lemon','watermenol']
#fruits.reverse()
#print(fruits)

#Ro'yxatni uzunligini qaytarish

#fruits = ['banan', 'lemon', 'watermelon','panda']
#print("The length of the list is : ", len(fruits))

#sonlar = list(range(0,10))
#print(sonlar)
#juft_sonlar = list(range(0,20,2))
#toq_sonlar = list(range(1,20,2))
#print(juft_sonlar)
#print(toq_sonlar)
#narxlar = [12000,15000,-24.7, -50,5000]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("Eng arzon narx: ",arzon, "Eng qimmat narx: ", qimmat, "Jami : ", jami)

#Tuples constant list

#tomonlar = (20,30,55.2)
#print(tomonlar)


#The fun part ( Amaliyot)
davlatlar = ['uzb', 'turkmaniston', 'tojikiston', 'russia', 'usa', 'italy']
print("Unsorted list: ",davlatlar)
print("Ro'yxatning uzunligi: ",len(davlatlar))
print("Sorted list: ", sorted(davlatlar))
print("Reversed sort: ", sorted(davlatlar,reverse=True))
print("Asl ro'yxat: ",davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print("Alifbo bo'yicha : ",davlatlar )
davlatlar.sort(reverse=True)
print("Alifbo ga teskari tartibda", davlatlar)
print(list(range(120,1200,2)))
juft_sonlar = list(range(120,1200,2))
yigindi = sum(juft_sonlar)
print("Yigindi: ", yigindi)
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)
ayirma = eng_katta - eng_kichik
print("Eng kattadan eng kichik ayirmas : ", ayirma)
print("Number of elements", len(juft_sonlar))
print("Boshidan 20 ta qiymat: ", juft_sonlar[:20])
print("O'rtasidan 20ta qiymat: ", juft_sonlar[12:22])
uzunlik = len(juft_sonlar)
oxirgi_20 = uzunlik - 20
print("Oxirgi yigirmata", juft_sonlar[520:-1])

taomlar = ["kuksi", "hamburge",'cheesburger','donar','sandwich']
nonushta = taomlar[:]
nonushta.remove("kuksi")
nonushta.remove("sandwich")
nonushta.append("karam shorva")
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
nonushta[0]="qaymoq va non"
print(nonushta)


