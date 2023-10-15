#21-dars. Funksiya va ro'yxat

#def bahola(ismlar):
#    baholar = {

#    }
#    while ismlar:
#        ism=ismlar.pop()
#        baho = input(f"Talaba {ism}ning bahosi: ")
#        baholar[ism]=int(baho)
#    return baholar
#talabalar = ['Ali','vali','hasan','husan']
#k = bahola(talabalar)
#print(k)    

#Homework1
def katta_harf(ism):
    for i in ism:
        print({i.title()})
    return i   
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)

#Homework2
def katta_harf(ism):
    for i in ism:
        print({i.title()})
    return i   
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)

#Homework3

talabalar = ['Ali', 'Vali', 'Hasan', 'Husan']
def lol(ism):
    baholar={}
    for i in ism:
        baho = input(f"Talaba {i}ning bahosini qoying: ")
        baholar[i]=baho
    return baholar
k = lol(talabalar)
print(k)   