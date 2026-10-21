#Dijital Ajanda

# gorevler={
# }
# def menu():
#     print("<----------MENÜ---------->")
#     print(f"{'1)Yeni Görev':<10}")
#     print(f"{'2)Mevcut Görevler':<10}")
#     print(f"{'3)Silme':<10}")
#     print(f"{'4)Çıkış':<10}")
# print(menu())

# def bir():
#     gorev=input("Lütfen eklemek istediğiniz görevi giriniz:")
#     if gorev in gorevler:
#         print("Bu görev zaten mevcut")
#         baska_islem()
#     elif gorev not in gorevler:
#         gorevler[gorev]=gorev
#         print(f"{gorev} görevi eklendi")
#         baska_islem()

# def iki():
#     print("Mevcut Görevler:")
#     for i, gorev in enumerate(gorevler, start=1):
#         print(f"{i}) {gorev}")
#     baska_islem()


# def uc():
#     silmek_istediginiz_gorev=input("Lütfen silmek istediğiniz görevi giriniz:")
#     if silmek_istediginiz_gorev in gorevler:
#         del gorevler[silmek_istediginiz_gorev]
#         print(f"{silmek_istediginiz_gorev} görevi silindi")
#         baska_islem()
#     elif silmek_istediginiz_gorev not in gorevler:
#         print("Böyle bir görev bulunamadı")
#         baska_islem()

# def dort():
#     print("Programdan çıkış yapılıyor...")

# def baska_islem():
#     yapmak_istediginiz_islem=input("Başka işlem yapmak istiyormusunuz (EVET / HAYIR):").upper()
#     if yapmak_istediginiz_islem=="EVET":
#         menu()
#     elif yapmak_istediginiz_islem=="HAYIR":
#         print("İyi günler")


# secim=input("Lütfen yapmak istediğiniz işlemi seçiniz:").upper()
# if secim=="1" or secim=="BİR":
#     bir()
# elif secim=="2" or secim=="İKİ":
#     iki()
# elif secim=="3" or secim=="ÜÇ":
#     uc()
# elif secim=="4" or secim=="DÖRT":
#     dort()


#Döviz Çevirici Gişe
# dolar=49.34 
# euro=52.34
# sterlin=61.34

# musteri_miktar_girisi = 0.0
# musteri_para_cevirme = ""
# def kullanici_islem():
#     musteri_miktar_girisi=float(input("Çevirmek istediğiniz miktarı giriniz:"))
#     musteri_para_cevirme=input("Hangi türe çevirmek istersiniz:").lower()
#     return musteri_miktar_girisi,musteri_para_cevirme

# def baska_islem():
#     baska_islem_yapmak=input("Başka işlem yapmak istiyormusunuz (EVET / HAYIR):").upper()
#     if baska_islem_yapmak=="EVET":
#         pass
#     elif baska_islem_yapmak=="HAYIR":
#         print("İşleminiz tamamlandı...")
# def cevirme_tutari():
#     ne_kadari_cevirme = float(input(f"Paranızın ne kadarını {musteri_para_cevirme} çevirelim: "))
    
#     if ne_kadari_cevirme > musteri_miktar_girisi:
#         ne_kadari_cevirme = float(input(f"Girdiğiniz miktar ilk başta girdiğiniz miktardan fazla || Paranızın ne kadarını çevirelim: "))
#         if ne_kadari_cevirme > 0 and ne_kadari_cevirme <= musteri_miktar_girisi:
#             print(f"Paranızın  {ne_kadari_cevirme} TL'si {cevirme:.2f} Dolar'a çevrildi kalan paranız: {musteri_miktar_girisi-ne_kadari_cevirme} TL")
#     elif ne_kadari_cevirme == 0:
#         print("Tutarı sıfır girdiniz")
#         return 0
#     elif ne_kadari_cevirme > 0 and ne_kadari_cevirme <= musteri_miktar_girisi:
        
#         cevirme=ne_kadari_cevirme/dolar
#         print(f"Paranızın  {ne_kadari_cevirme} TL'si {cevirme:.2f} Dolar'a çevrildi kalan paranız: {musteri_miktar_girisi-ne_kadari_cevirme} TL")
        

# def dolar(cevrilen_tutar):
#     dolar_cevirme=cevrilen_tutar/dolar
#     print(f"Paranızı çevirebileceğiniz son tutar:{dolar_cevirme:.2f}Dolar")
    
# def euro(cevrilen_tutar):
#     euro_cevirme = cevrilen_tutar/ euro
#     print(f"Paranızı çevirebileceğiniz son tutar: {euro_cevirme:.2f} Euro")
# def sterlin(cevrilen_tutar):
#     sterlin_cevirme = cevrilen_tutar / sterlin
#     print(f"Paranızı çevirebileceğiniz son tutar: {sterlin_cevirme:.2f} Sterlin")

# def menu():
#     devam=True
#     while devam:
#         kullanici_islem()
#         tutar=cevirme_tutari()
#         if tutar>0:
#             if musteri_para_cevirme=="dolar":
#                 dolar(tutar)
#             elif musteri_para_cevirme=="euro":
#                 euro(tutar)
#             elif musteri_para_cevirme=="sterlin":
#                 sterlin(tutar)
#             else:
#                 print("Geçersiz para birimi")
#         devam=baska_islem()

# menu()

    


#ATM Pin kırıcı Simülasyonu
"""
gizliKod=1234
can=5
def hak():
while can>0:
can-=1


"""