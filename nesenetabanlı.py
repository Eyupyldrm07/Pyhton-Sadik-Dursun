# class galeri:
#     arac_ismi='ferrarri'
#     km_degeri = 9500
#     renk = 'kirmizi '

#     def araba_ozellikleri(self):
#         print(f'arac ismi: {self.arac_ismi}\nkm degeri:{self.km_degeri}\nRenk bilgisi: {self.renk}')


# tuncay_otamativ =galeri()

# tuncay_otamativ.araba_ozellikleri()
# print('-'*45)
# fatih_otomativ = galeri()
# fatih_otomativ.araba_ozellikleri()




class okul:
 
    def __init__(self,sube,ogretmen,bolum,mevcut,maas):
        self.sube =sube
        self.ogretmen=ogretmen
        self.bolum=bolum
        self.mevcut=mevcut
        self.maas=maas




    def bilgiler_goster(self):
        print('-'*45)
        print('Sinif bilgileri')
        print('Sube:{}\nOgretmen:{}\nBolum:{}\nSinif Mevcudu:{}'.format(self.sube,self.ogretmen,self.bolum,self.mevcut))

    def brans_degis(self):
        yeni_brans =input('Lutfen Yeni Branisinizi Yaiziniz:')
        print('***Eski Brnas***',self.bolum)
        self.bolum = yeni_brans
        print('-'*45)
        print('Sinif bilgileri')
        print('Sube:{}\nOgretmen:{}\nBolum:{}\nSinif Mevcudu:{}'.format(self.sube,self.ogretmen,self.bolum,self.mevcut))
        print('-'*45)
    def maas_goster(self):
        print(f'{self.ogretmen} adli ogretmenin maasi:{self.maas} tL')



class mudur(okul):
    print('Yonetici Paneli')

    def __init__(self, sube, ogretmen, bolum, mevcut,maas,kidem):
        super().__init__(sube, ogretmen, bolum, mevcut,maas)
        self.kidem = kidem


    def bilgiler_goster(self):
        print('-'*45)
        print('Sinif bilgileri')
        print('Sube:{}\nOgretmen:{}\nBolum:{}\nSinif Mevcudu:{}'.format(self.sube,self.ogretmen,self.bolum,self.mevcut))

    def zam_yap(self):
        print(f'Zam ekranina hosgeldiniz Sayin: {self.ogretmen}')
        zam_miktari = int(input('Lutfen Maas MIktarini TL cinsinden yaziniz:'))
        self.maas = int(self.maas) + zam_miktari
        print(f'{self.ogretmen}adli ogretmenin maasina {zam_miktari} kadar zam yapildi. ')
        print(f'{self.ogretmen}adli ogretmenin guncel maasi {self.maas}')

yonetici = mudur('11','Tuncay','fizik','49','4500','Mudur yardimcisi')

sinif_adi=input('Lutfen sube numarisini giriniz')
ogretmen_bilgisi=input('Lutfen isminizi giriniz')
bolum_a1=input('Lutfen bransinizi giriniz')
maas_miktari=int(input('Lutfen maas miktarini  giriniz'))
print('Bu alani sadece yonetici iseniz doldururnuz')
kidem_al=input('Lutfen kidem seviyenizi giriniz')
if not kidem_al:
    print('Ogretmen Kounumundasiniz')



sinif_olusturma=input('Sinif olusturunuz')

while True:
    if not kidem_al:
        sinif_olusturma=okul(sinif_adi,ogretmen_bilgisi,bolum_a1,maas_miktari)
        soru_sor=input('1-Bilgileri Goster\n2-Maasi Goster\n3-Bransu Goster')
        if soru_sor=='1':
            sinif_olusturma.bilgiler_goster()
        elif soru_sor=='2':
            sinif_olusturma.maas_goster()
        elif soru_sor=='3':
            sinif_olusturma.brans_degis()
        else:
            print('Gecerli bi sayi giriniz..')
            









# while True:
#    secim_yap=input('1-Ogretmen Girisi\n2-Yonetici girisi\n')
#    if secim_yap == '1':
#        sinif_adi=input('Lutfen sube numarisini giriniz')
#        ogretmen_bilgisi=input('Lutfen isminizi giriniz')
#        bolum_a1=input('Lutfen bransinizi giriniz')
#        mevcut=input('Lutfen sinif mevcudunu  giriniz')
#        maas_miktari=input('Lutfen maas miktarini  giriniz')
#        sinif_olusturma=input('Sinif olusturunuz')

#        sinif_olustur = okul(sinif_adi,ogretmen_bilgisi,bolum_a1,mevcut,maas_miktari)

#        print('Sinifiniz olusturuldu')
#        tercih_yap=input('1-Bilgileri  Goster:\n2-Brans Degistir:\n3-Maas Goster')
#        if tercih_yap==1:
#         sinif_olustur.bilgiler_goster()
#        elif tercih_yap==2:
#            sinif_olustur.brans_degis()
#        elif tercih_yap==3:
#            sinif_olustur.maas_goster()
#        else:
#            print('Cikis yapildi')
#            break
       
#    if secim_yap == '2':
#        sinif_adi=input('Lutfen sube numarisini giriniz')
#        ogretmen_bilgisi=input('Lutfen isminizi giriniz')
#        bolum_a1=input('Lutfen bransinizi giriniz')
#        mevcut=input('Lutfen sinif mevcudunu  giriniz')
#        maas_miktari=input('Lutfen maas miktarini  giriniz')
#        sinif_olusturma=input('Sinif olusturunuz')
#        kidem_al=input('Kidem yaziniz')

#        sinif_olustur = mudur(sinif_adi,ogretmen_bilgisi,bolum_a1,mevcut,maas_miktari,kidem_al)

#        print('Yonetici Sinifiniz olusturuldu')
#        soru_sor = input('1-Bilgileri Goster \n2-Zam yap\n')
#        if soru_sor==1:
#         sinif_olustur.bilgiler_goster()
#        elif soru_sor==2:
#            sinif_olustur.zam_yap()
#        else:
#            print('Cikis yapildi')
#            break
       


    
    
