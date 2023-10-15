#17-dars While tsikli 
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur !!!")
#savol = "Istalgan sonni kiriting>>>"
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print("Dastur")

#break for
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")

#son = 0 
#while son<10:
#    son += 1
#    if son%2 == 0:
#        continue
#    else:
#        print(son)

#son = 1
#while son<=5:
#    print(son,end="")
#    son = son+1

#Homework time , It is gonna be fun and this one will be in english , I hope

#yaxshi = "Yaxshi ko'rgan kitoblaringizni kiriting: "
#yaxshi += "To'xtatish uchun 'stop' deb yozing: "
#while True:
#    qiymat = input(yaxshi)
#    if qiymat=='stop':
#        break
#    else:
#        print(f"Sizning yaxshi ko'rgan kitobingiz nomi {qiymat}")
#print("Dastur yakunlandi!!!")


#example#2
#yosh = "Yoshingizni kiring "
#yosh += "To'xtash uchun 'exit' so'zini kiriting: "  
#while True:
#    yaxshi = input(yosh)
#    if yaxshi == 'exit':
#        break  
#    qiymat = int(yaxshi)   
#    if qiymat<=7:
#        print(f"{qiymat} dan yoshlarga -2000 so'm")
#    if qiymat>=7 and qiymat<=18:
#        print(f"7-18 gacha 3000 so'm")   
#    if qiymat>=18 and qiymat<=65:
#        print("18-65 gacha 10000 so'm")
#    if qiymat>=65:
#        print("65 dan kattalarg bepul")
#print("Dastur tugadi")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='Exit':
        break
    yosh = int(qiymat)
    if yosh<0:
        continue
    else:
        ildiz = float(yosh)**(0.5)
        print(f"{yosh} ning ildizi {ildiz} ga teng")
