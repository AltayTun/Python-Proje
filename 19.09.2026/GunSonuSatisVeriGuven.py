urunAd = input("Ürün adını giriniz: ")
katagori = input("Kategoriyi giriniz: ")
fiyat = float(input("Fiyatını giriniz: "))
adet = int(input("Adedini giriniz: "))

#Günlük Liste
urunler={
    urunAd:{
        "Katagori":katagori,
        "Fiyat":fiyat,
        "Adet":adet
    },
    "Bilgisayar":{
        "Katagori":"Elektronik",
        "Fiyat":3.500,
        "Adet":5
    },
    "Fare":{
            "Katagori":"Elektronik",
            "Fiyat":350,
            "Adet":100
        }
}

gunluk="Günlük satış listeniz"
sonuc=gunluk.center(50,"-").upper
print(urunler)
kopya=urunler.copy()
b="Kopya Listeniz"
a=b.center(50,"-")
print("Kopya")
import copy
kopya = copy.deepcopy(urunler)

print("\n" + " DOĞRUDAN GÜNCELLEME/EKLEME ".center(50, "-"))
degisecek_urun = input("Güncellenecek veya eklenecek ürün adı: ")
yeni_katagori = input("Kategori: ")
yeni_fiyat = float(input("Fiyat: "))
yeni_adet = int(input("Adet: "))

# if-else veya try-except olmadan direkt atama yapıyoruz. 
# Ürün varsa güncellenir, yoksa sıfırdan eklenir.
kopya[degisecek_urun] = {
    "Katagori": yeni_katagori,
    "Fiyat": yeni_fiyat,
    "Adet": yeni_adet
}

print("\nOrijinal Liste:", urunler)
print("Kopya Liste:   ", kopya)
