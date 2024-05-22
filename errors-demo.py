liste = ['1','2','5a','10b','abc','10','50']

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue


# while True:
#     sayi = input('sayi: ')
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print('girdiginiz sayi: ',result)
#     except ValueError:
#         print('Gecersiz sayi')
#         continue

# def checkPassword(parola):
#     turkce_karakterler = 'şçğüıİ'
   

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('parola turkce karekter icerkemektedir.')
#     else:
#         pass

# print('gecerli parola ')

# parola = input('parola: ')
# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)





def faktoriyel(x):
    x =int(x)

    if x<0:
        raise ValueError ('negatif deger')
    
    result = 1

    for i in range (1,x+1):
        result *=i

    return result
for x in [5,10,20,-3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)

   





