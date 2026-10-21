urunAd = input("Ürün adını giriniz: ")
katagori = input("Kategoriyi giriniz: ")
fiyat = float(input("Fiyatını giriniz: "))
adet = int(input("Adedini giriniz: "))

urunler={
    urunAd:{
        "Katagori":katagori,
        "Fiyat":fiyat,
        "Adet":adet
    },
    "Bilgisayar":{
        "Katagori":"Elektronik",
        "Fiyat":1500,
        "Adet":5
    }
}
aranan_urun=input("Urunler Listesinde bulunan bir ürünü giriniz:")
var=urunler[aranan_urun]
print(var)