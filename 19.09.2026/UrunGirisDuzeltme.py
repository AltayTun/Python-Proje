urunAd = input("Ürün adını giriniz: ")
katagori = input("Kategoriyi giriniz: ")
fiyat = float(input("Fiyatını giriniz: "))
adet = int(input("Adedini giriniz: "))
duzenAd=urunAd.strip().capitalize()
duzenKat=katagori.strip().capitalize()

urunler = {
    duzenAd: {
        "Kategori": duzenKat,
        "Fiyat": fiyat,
        "Adet": adet
    }
}
print(urunler)
