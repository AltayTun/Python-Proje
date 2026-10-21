#1
def daire_alani(yaricap):
    return 3*yaricap**2

print(daire_alani(5))

#2
def kare_toplami(a,b):
    return a**2 + b**2
print(kare_toplami(10,20))

#3
def sinirsiz_toplam(*sayilar):
    toplam=0
    for sayi in sayilar:
        toplam+=sayi
    return toplam

print(sinirsiz_toplam(10,20,30))

#4
def araba_tanit(**ozellikler):
    for key,value in ozellikler.items():
        print(f"{key}:{value}")
araba_tanit(marka="Toyota")

#başka yol

def araba_tanit(**ozellikler):
    metin=""
    for key, value in ozellikler.items():
        metin+= f"{key}:{value}\n"
    return metin
print(araba_tanit(marka="toyota"))

#5
def pahali_ürünleri_bul(urun_sozlugu):
    for isim,deger in urun_sozlugu.items():
        if deger>30:
            print(f"{isim}:{deger}")

fiyatlar = {"Elma": 15, "Muz": 40, "Ekmek": 10, "Et": 250}
pahali_ürünleri_bul(fiyatlar)