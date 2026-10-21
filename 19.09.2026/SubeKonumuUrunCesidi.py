urunAd = input("Ürün adını giriniz: ")
katagori = input("Kategoriyi giriniz: ")
fiyat = float(input("Fiyatını giriniz: "))
adet = int(input("Adedini giriniz: "))

urunler={
    urunAd:{
        "Katagori":katagori,
        "Fiyat":fiyat,
        "Adet":adet
    }
}
konum=("Sakarya","Adapazarı")
sirali_anahtarlar = sorted(urunler)
ilk_urun = sirali_anahtarlar[0]
print("\n--- Ürün Bilgileri ---")
print(f"Ürün Adı: {ilk_urun}")
print(f"Kategori: {urunler[ilk_urun]['Katagori']}")
print(f"Fiyat: {urunler[ilk_urun]['Fiyat']}")
print(f"Adet: {urunler[ilk_urun]['Adet']}")
print(f"Konum:{konum[0]}")
