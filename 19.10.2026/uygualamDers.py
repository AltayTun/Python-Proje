# # #1
# stoklar = {
#     "laptop": 5,
#     "mouse": 2,
#     "klavye": 12,
#     "monitor": 0,
#     "kulaklık":3
# }
# print("Stoktakileri görmek için: 1":<20)
# print("Stokta olmayanları görmek için: 2":<20)
# print("Stoğu tükenmekte olanlar için: 3":<20)
# secim=input("Seçiminiz:")
# if secim == "1":
#     for urun, miktar in stoklar.items():
#         if miktar > 0:
#             print(f"{urun}: {miktar} adet")

# elif secim == "2":
#     for urun, miktar in stoklar.items():
#         if miktar == 0:
#             print(f"{urun}: {miktar} adet")
# elif secim=="3":
#     for urun,miktar in stoklar.items():
#         if miktar<=3:
#             print(f"{urun}:{miktar} adet")

# else:
# print("Yanlış bir seçim yaptınız")
# # 2
butce = float(input("Toplam bütçenizi giriniz:"))
urunler = [
    {"ad": "laptop", "fiyat": 30000},
    {"ad": "mouse", "fiyat": 1000},
    {"ad": "klavye", "fiyat": 2000},
    {"ad": "monitor", "fiyat": 8000},
]
uygun_urun_bulundu = False
for urun in urunler:
    if urun["fiyat"] <= butce:
        print(f"{urun['ad']}: {urun['fiyat']}")
        uygun_urun_bulundu = True

if not uygun_urun_bulundu:
    print("Bütçenize uygun herhangi bir ürün bulunamadı")


for i in range(len(urunler)):
    for j in range(i + 1, len(urunler)):
        birinci = urunler[i]
        ikinci = urunler[j]

        toplam_fiyat = birinci["fiyat"] + ikinci["fiyat"]

        if toplam_fiyat <= butce:
            print(
                f"{birinci['ad']} + {ikinci['ad']} alabilirsiniz. (Toplam: {toplam_fiyat} TL)"
            )
# 3
siparisler = [
    {
        "musteri": "test",
        "urunler": [{"urunadi": "laptop", "urunfiyati": 25000, "urunadedi": 5}],
    },
    {
        "musteri": "emre",
        "urunler": [{"urunadi": "Telefon", "urunfiyatı": 10000, "urunadedi": 2}],
    },
]
musteri_adi = input("Müsteri adını giriniz")
for siparis in siparisler:
    if musteri_adi == siparis["musteri"]:
        for urun in siparis["urunler"]:
            toplam = urun["urunfiyati"] * urun["urunadedi"]
            print(f"Toplam tutar:{toplam}")
        break
    else:
        print("Aradığınız müşteri listede yok")
        break


# 4
stoklar = [
    {
        "kategori": "Elektronik",
        "urunler": [
            {"ad": "laptop", "fiyat": 25000, "adet": 10},
            {"ad": "mouse", "fiyat": 1000, "adet": 25},
            {"ad": "klavye", "fiyat": 2000, "adet": 15},
        ],
    },
    {
        "kategori": "Giyim",
        "urunler": [
            {"ad": "tshirt", "fiyat": 500, "adet": 50},
            {"ad": "pantolon", "fiyat": 1200, "adet": 30},
        ],
    },
    {
        "kategori": "Kirtasiye",
        "urunler": [
            {"ad": "defter", "fiyat": 150, "adet": 100},
            {"ad": "kalem", "fiyat": 50, "adet": 200},
        ],
    },
]

for kat in stoklar:
    print(kat["kategori"])

secilen = input("Kategori: ").lower()

for kat in stoklar:
    if kat["kategori"].lower() == secilen:
        for urun in kat["urunler"]:
            print(urun)

        alinan_urun = input("Urun: ")
        alinan_adet = int(input("Adet: "))

        for urun in kat["urunler"]:
            if urun["ad"] == alinan_urun:
                urun["adet"] -= alinan_adet
                print("Kalan stok:", urun["adet"])
