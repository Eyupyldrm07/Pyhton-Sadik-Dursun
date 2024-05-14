# sehirler = {'kocaeli' : 41 , 'istanbul' :34}
# print(sehirler['istanbul'])
# print(sehirler['kocaeli'])

# sehirler['ankara'] = 6
# print(sehirler['ankara'])


# users = {
#     'sadikturan' : {
#         'age':36,
#         'email':'asfasdfasfsa',
#         'adress':'kocaeli',
#         'phone':'123456'
#     },
#     'eyupyildirim':{
#         'age':24,
#         'email':'aeeeeee',
#         'adress':'kilis',
#         'phone':'123456'}
# }

# print(users['sadikturan']['age'])
# print(users['sadikturan']['email'])
# print(users['sadikturan']['adress'])
# print(users['sadikturan']['phone'])



# ogrenciler = {
#     '101': 
#     {
#         'ad': input('Adinizi giriniz'),
#         'soyad': input('Soyadinizi giriniz'),
#         'Telefon': input('Telefon numaranizi giriniz giriniz')

#     },
#     '102':  {
#         'ad': input('Adinizi giriniz'),
#         'soyad': input('Soyadinizi giriniz'),
#         'Telefon': input('Telefon numaranizi giriniz giriniz')

#     },
#     '103':  {
#         'ad': input('Adinizi giriniz'),
#         'soyad': input('Soyadinizi giriniz'),
#         'Telefon': input('Telefon numaranizi giriniz giriniz')

#     }
# }
# print(ogrenciler['101'])
# print(ogrenciler['102'])
# print(ogrenciler['103'])

# ogrenciler = {}
# number =input('numarani gir')
# name =input('adini gir')
# surname =input('soyadini gir')
# phone =input('telefonunu gir')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad':surname,
#     'phone':phone
# }

# ogrenciler = {}
# number =input('numarani gir')
# name =input('adini gir')
# surname =input('soyadini gir')
# phone =input('telefonunu gir')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad':surname,
#     'phone':phone
# }

# ogrenciler = {}
# number =input('numarani gir')
# name =input('adini gir')
# surname =input('soyadini gir')
# phone =input('telefonunu gir')

# ogrenciler[number] = {
#     'ad': name,
#     'soyad':surname,
#     'phone':phone
# }

# print(ogrenciler)

# ogrNo = input('ogrenci no ')
# ogrenci = ogrenciler[ogrNo]
# print(ogrenci)




# x, y, z = 2, 5, 107

# numbers =1, 5, 7, 10, 6

# sayi1=int(input('Bir sayi giriniz:'))
# sayi2=int(input('Bir sayi giriniz:'))

# carpim = (sayi1 * sayi2)
# toplam = (x + y + z)
# fark = (carpim - toplam)
# print(fark)


# bolum =  (y // x)
# print(bolum)

# toplam = (x + y + z )
# mod = (toplam % 3 )
# print(mod)

# us = (y ** x)
# print(us)



# vize = int(input('Vize notunuzu giriniz'))
# final = int(input('Final notunuzu giriniz'))


# result = (vize % 60) +(final % 40)
# if result > 50 :
#     print('Sinavi gectiniz')
# else:
#     print('sinavdan kaldiniz')



# vize = input('Vize notunuzu giriniz')
# final = input('Final notunuzu giriniz')


# if vize == ('a@gmail.com') :
#     if final == ('01234'):
#         print('hosgeldiniz')
#     else:
#              print('kulanici adi veya parola yanlis')



# name = str(input('Adinizi giriniz'))
# age = int(input('Yasinizi Giriniz'))

# if age > 18 :

#     diploma = str(input('Lutfen sahip oldugunuz diplomayi giriniz'))

#     if diploma == ('universite') :
#           print('Ehliyet alabilirsiniz')
#     elif diploma == ('lise') :
#              print('Ehliyet alabilirsiniz')
#     else :
#           print('Yeterli diploma duzeyine sahip degilsiniz')

# else:
#     print(f'Sayin {name} Yasiniz ehliyet almak icin yeterli degil. {-(age-18)} yil sonra alabilirsiniz. ')





# vize1 = float(input('Vize 1 notunuzu giriniz'))
# vize2 = float(input('Vize 2 notunuzu giriniz'))
# Final = float(input('Final notunuzu giriniz'))


# result = ((vize1+vize2+Final)/3)

# if (result >= 0) and (result <= 24) :
#     print('Sonucunuz 0') 

# elif (result >= 25) and (result <= 45) :
#     print('Sonucunuz 1') 

# elif (result >= 45) and (result <= 54) :
#     print('Sonucunuz 2') 

# elif (result >= 55) and (result <= 69) :
#     print('Sonucunuz 3') 

# elif (result >= 70) and (result <= 85):
#     print('Sonucunuz 4') 

# elif (result >= 86) and (result <= 100) :
#     print('Sonucunuz 5') 
# else:
#     print('Ortalama yanlis hesaplanmis')

