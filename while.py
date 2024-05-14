# x = 1
# while x <= 100:
#     if x % 2==1:
#         print(f'sayi tek {x}')  
#     elif x % 2==0:
#         print(f'sayi cift {x}')  
#     x+=1
      
# print('Bitti.....')



# name = ''
# while not name :
#     name =input('isminizi giriniz: ')

# print(f'merhaba {name}')

# sayilar =[1,3,5,7,9,12,19,21]

# i = 0

# while i< len(sayilar):
#     print(sayilar[i])
#     i+=1




# start =int(input('Baslangic sayisi giriniz'))
# finis =int(input('Bitis sayisi giriniz'))

# result = start
# while result < finis:
#     result+=1
#     if (result%2==1):
#         print(result)

# i = 101
# while 2 <= i  :
#     i -= 1
#     print(i)


# sayi1 = int(input('sayi 1 i giriniz ')),
# sayi2 = int(input('sayi 2 i giriniz ')),
# sayi3 = int(input('sayi 3 i giriniz ')),
# sayi4 = int(input('sayi 4 i giriniz ')),
# sayi5 = int(input('sayi 5 i giriniz ')),


# numbers = []

# i= 0 

# while i < 5:
#     sayi =int(input('sayi: '))
#     numbers.append(sayi)
#     i+=1

# numbers.sort()
# print(numbers)



# urunler = []

# i = 0
# sayi=int(input('Kac adet urun istiyorsunuz'))
# while i < sayi :
#      i+=1
#      name =input('Urun Name: ')
#      price=int(input('Urun fiyati'))
#      urunler.append({
#           'name':name,
#           'price':price
#      })

   

# for urun  in urunler:
#      print(f'urun adi {urun['name']} urunun fiyati {urun['price']}')


# import random

# sayi = random.randint(1,100)
# can =int(input('kac adet caniniz olmasini istersiniz.'))
# hak = can
# sayac =0 

# while hak > 0:
#     hak-=1
#     sayac +=1
#     tahmin = int(input('tahmin:'))

#     if sayi == tahmin:
#         print(f'Tebrikler {sayac}. sefer de bildiniz.toplam puaniniz {100-(100/can)*(sayac-1)}')
#         break
#     elif sayi>tahmin:
#         print('Yukari')
#     else:
#         print('asagi')

#     if hak == 0 :
#         print(f'hakkiniz bitti . tututal sayi : {sayi} ')



# sayi = int(input('Bir sayi giriniz:'))
# asalmi = True

# if sayi ==1:
#     asalmi=False

# for i in  range (2,sayi):
#      if sayi % i ==0 :
#          asalmi= False
#          break
# if asalmi:
#     print('sayi asaldir')
# else:
#     print('asal degildir')


