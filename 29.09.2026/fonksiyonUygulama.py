#1
def cay_demle(bardak_boyutu="Çay bardağı",sertlik="Orta"):
    print("Çayınız hazırlanıyor.")
    if sertlik=="Orta":
        print(f"Çayınız {sertlik} ve {bardak_boyutu}")
    else:
        print(f"Çayınız {sertlik} ve {bardak_boyutu}")

cay_demle(sertlik="Az")
cay_demle()

#2
def kargo_tasi(*cuval):
    print(f"Hasan hoşgeldin görevin {len(cuval)} kadar kutu taşımak")
    for tasi in cuval:
        print(f"- {tasi} kutu taşıdım")
kargo_tasi(6)

#3
def personel_kayit(**personel_bilgi):
    print("Bilgiler dizildi.")
    for index,kayit in personel_bilgi.items():
        print(f"{index}={kayit} arşive dizildi")
personel_kayit(İsim="Emre",Soyad="Altun",Maaş=50000)
print("-"*30)
#4
def prim_hesapla(satis_miktari,urun_fiyati):
    toplam_ciro=satis_miktari*urun_fiyati
    prim_tutari=toplam_ciro*0.10
    return toplam_ciro,prim_tutari
ciro,prim=prim_hesapla(10,1000)
print(f"Şirketin bu ayki toplam cirosu:{ciro:,}TL".replace(",","."))
print(f"Bu ayki prim:{prim}")