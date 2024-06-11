import sqlite3

db =sqlite3.connect('Kitaplar.db')

yetki = db.cursor()

kitap_adi=input('Kitabin adini giriniz:')
kitap_sayfaNosu = input('Kitabin sayfa nosunu giriniz:')
kitap_yili = input('Kitabin yilini giriniz:')

yetki.execute('CREATE TABLE IF NOT EXISTS tuncay (isim ,sayfa,kitab yili )')
yetki.execute(f'INSERT INTO tuncay VALUES ("{kitap_adi}","{kitap_sayfaNosu}","{kitap_yili}")')
yetki.execute('SELECT *FROM tuncay')

yazdir = yetki.fetchall() # Butun veri tabani verileri ile islem yapmak istiyorsak kullaniriz.
# yazdir = yetki.fetchmany() #ile veritabanin da belirli sayida veri cekmek icin kullaniriz





# print(yazdir)
# say = 1
# for i  in yazdir:
#     print(f'{say}: Kitap adi :{i[0]}\nKitap Sayfa sayisi :{i[1]}\nKitap Yili:{i[2]}\n')
#     say+=1

# db.commit()






# print(f'Kitap eklendi:{kitap_adi}')
db.close()