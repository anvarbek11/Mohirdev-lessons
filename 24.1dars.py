#Oyin yaratish
import random
def son_top(x=10):
    son=random.randint(1,x)
    print(son)
    taxminlar=0
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi? ")
    while True:
        taxminlar += 1
        user=int(input("<<<<<<"))
        if user>son:
            print("Men o'ylagan son bundan kichikroq edi yana harakat qiling: ")
        elif user<son:
            print("Men o'ylagan son bundan kattaroq edi yana harakat qiling:  ")    
        else:
            print("Siz bu sonni topdingiz ")
            break
    print(f"Tabriklaymiz . {taxminlar} - da topdingiz")
    return taxminlar

def son_oyla(x=10):
    print(f"Men 1 dan {x} gacha son o'ylang men topishga harakat qilaman: ")
    quyi=1
    yuqori=x
    taxminlar = 0
    while True:
         taxminlar += 1
         son1=random.randint(quyi,yuqori)
         print(f"Siz {son1} sonini o'ylagandingiz: to'g'ri (T), men oylagan son bundan kattaroq bo'lsa (+), yoki kichikroq bo'lsa (-) - ")
         user = input(">...")
         if user == '+':
            quyi = son1+1
         elif user=='-':
            yuqori=son1-1
         else:
            break
    print(f"Tabriklaymiz siz buni {taxminlar}-da topdishingiz ")
    return taxminlar

def solishtirish(x=10):
    yana=True
    while yana:
        tamin_me=son_top(x)
        tamin_ko=son_oyla(x)
        if tamin_ko>tamin_me:
            print("Men yutdim!")
        elif tamin_ko<tamin_me:
            print("Siz yutdingiz!")
        else:
            print("Durrang")
        yana =int(input("Yana o'ynaysizmi XA(1)/yoq(0)"))
solishtirish()       



            

    
        
    



            

        


        

