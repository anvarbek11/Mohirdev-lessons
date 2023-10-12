#14-lesson Lug'at bilan tanishuv -> Dictionary

#car_0 = {"model": "ferrari", "rang" : "qizil"}
#print(car_0["model"])
#print(car_0["rang"])

#en_uz = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
#print(en_uz["apple"])

#mevalar = {"olma":10000, "tarvuz":8000, "qovun":10000}
#print(f"Olma narhi {mevalar['olma']} ga teng")

#talaba_0 = {"ism":"murod olimov", "yosh":20, "t_yil":2000}
#print(f"{talaba_0['ism'].title()},\
#      {talaba_0['t_yil']},\
#{talaba_0['yosh']}")
#talaba_0['kurs'] = 4
#talaba_0['fakultet'] = 'informatika'

#talaba_1 = { }
#talaba_1['ism'] = 'qobil rasulov'
#talaba_1['kurs'] = 3
#talaba_1['yosh'] = 4
#print(talaba_1)
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")

#talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']} - kurs")

#talaba_0 = {'lol':1,'model':'ferrari'}
#print(talaba_0)
#del talaba_0['lol']
#print(talaba_0)
#meva = talaba_0.get('lol', 'Bunday narsa mavjud emas')
#print(meva)

#talaba_0['kurs'] = 4
#print(talaba_0)

#empty dictionary
#talaba = {

#}
#talaba['sardor'] = 21
#talaba['lappa'] = 15
#print(talaba)

#Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa, shu ketme - ketlik saqlanib qoladi
#talaba = {'s':'Sarvar sawa'}
#talaba['kurs'] = 4
#print(f"Talaba {talaba['s'].title()} {talaba['kurs']} - da o'qiydi")
#del talaba['s']
#print(talaba)

#telefonlar = {
#    'ali':'iphone x',
#    'vali':'galaxy s9',
#    'olim':'mi 10 pro',
#    'orif':'nokia 3310'
#}
#phone = telefonlar.get('hasan','Bunday ism mavjud emas !')
#print(phone)

#Homework time

#oila = {'otam':'Odilbek',
#        't_yil': '1965',
#        'address':'Xorazm viloyati'}
#print(f"Otamning ismi {oila['otam']}, {oila['t_yil']} - yilda {oila['address']}-da tug'ilgan")

#taomlar = {'ism':'asror','ovqat':'shashlik',
#           'ism1':'dildora','ovqat1':'mangal',
#           'ism2':'dilrabo','ovqat2':'somsa',
#           'ism3':'odilbek','ovqat3':'gosht',
#           'ism4':'sevara','ovqat4':'pizza'}
#print(f"{taomlar['ism']}ning sevimli taomi {taomlar['ovqat']}")
#print(f"{taomlar['ism1']}ning sevimli taomi {taomlar['ovqat1']}")
#print(f"{taomlar['ism2']}ning sevimli taomi {taomlar['ovqat2']}")

#python = {'integer':'butun son',
#          'float':'onlik son',
#          'string':'matn',
#          'if':'agar',
#          'else':'aksincha',
#          'in':'ichida',
#          'for':'uchun',
#          'error':'xato',
#          'type':'turi',
#          'true':'togri'}
#soz = input("Biror so'z kiritng >>> ")
#bor = python.get(soz,"Bunday so'z mavjud emas")
#print(bor)

python = {'integer':'butun son',
          'float':'onlik son',
          'string':'matn',
          'if':'agar',
          'else':'aksincha',
          'in':'ichida',
          'for':'uchun',
          'error':'xato',
          'type':'turi',
          'true':'togri'}
soz = input("Biror so'z kiritng >>> ")
if soz == 'integer':
    print("Integer bu butun son")
if soz == 'float':
    print("Flaot so'zi onlik son deb tajima qilinadi")
if soz == 'string':
    print("String so'zi matn deb tarjima qilinad")
else:
    print("Bunday so'z mavjud emas")

