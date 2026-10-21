urunAd = input("Ürün adını giriniz: ")
katagori = input("Kategoriyi giriniz: ")
fiyat = float(input("Fiyatını giriniz: "))
adet = int(input("Adedini giriniz: "))

#firmamız
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
a="Ürünler listeniz burada"
b=a.center(50,"*")
print(b)
benzersiz=set(urunler)
son=str(benzersiz).center(50)
print(son)

#rakip firma
uruns={
    "Fare":{
        "Katagori":"Elektronik",
        "Fiyat":"750",
        "Adet":250
    },
    "Bilgisayar":{
        "Katagori":"Elektronik",
        "Fiyat":"4.000",
        "Adet":25
    },
    "Kulaklık":{
        "Katagori":"Elektronik",
        "Fiyat":"1000",
        "Adet":50
        }
}
ortak_urun=set(urunler)&set(uruns)
print(f"Rakip Firma ile Firmamızın ortak ürünleri:{ortak_urun}")
print("-"*20)
print("-"*20)
bizim=set(urunler)-set(uruns)
print(f"Rakip Firma ile Firmamızın farklı ürünleri:{bizim}")
