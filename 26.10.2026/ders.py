urunler = {
    1: {"ad": "Elma (1 kg)", "fiyat": 35.0},
    2: {"ad": "Muz (1 kg)", "fiyat": 60.0},
    3: {"ad": "Süt (1 L)", "fiyat": 32.5},
    4: {"ad": "Ekmek", "fiyat": 15.0},
    5: {"ad": "Yumurta (10'lu)", "fiyat": 55.0},
    6: {"ad": "Peynir (500 g)", "fiyat": 120.0},
    7: {"ad": "Zeytin (500 g)", "fiyat": 95.0},
    8: {"ad": "Domates (1 kg)", "fiyat": 30.0},
    9: {"ad": "Salatalık (1 kg)", "fiyat": 25.0},
    10: {"ad": "Pirinç (1 kg)", "fiyat": 70.0},
    11: {"ad": "Makarna", "fiyat": 20.0},
    12: {"ad": "Un (2 kg)", "fiyat": 65.0},
    13: {"ad": "Şeker (1 kg)", "fiyat": 45.0},
    14: {"ad": "Çay (1 kg)", "fiyat": 210.0},
    15: {"ad": "Kahve (100 g)", "fiyat": 150.0},
    16: {"ad": "Su (5 L)", "fiyat": 25.0},
    17: {"ad": "Meyve Suyu (1 L)", "fiyat": 40.0},
    18: {"ad": "Çikolata", "fiyat": 30.0},
    19: {"ad": "Bisküvi", "fiyat": 18.0},
    20: {"ad": "Deterjan (3 kg)", "fiyat": 250.0},
}
for deger,urun in urunler.items():
    print(f"ürünün adı:{urun['ad']} Ürün fiyatı: {urun['fiyat']} ")
kullanici_giris=int(input("Hangi ürünü görmek istiyorsunuz:"))


if kullanici_giris in urunler:
    secilen_urun = urunler[kullanici_giris]
    print(f"Ürün adı: {secilen_urun['ad']} Fiyat: {secilen_urun['fiyat']} TL")
else:
    print("Geçersiz bir ürün numarası girdiniz")


for deger, urun in urunler.items():
    print(f"ürünün adı:{urun['ad']} Ürün fiyatı: {urun['fiyat']} ")


sepet = []

while True:
    sepet_kullanici_giris = int(input("Ürün kodu giriniz:"))
    if sepet_kullanici_giris in urunler:
        secilen_urun = urunler[sepet_kullanici_giris]
        print(f"Ürün adı: {secilen_urun['ad']}  Fiyat: {secilen_urun['fiyat']} TL")
        sepet.append(secilen_urun)
        for urun in sepet:
            print(f"Ürün adı: {urun['ad']} Fiyat: {urun['fiyat']}" )
        # print("Ürün sepete eklendi.")
        # print(f"Güncel sepet:{sepet}")
    else:
        print("Geçersiz bir ürün numarası girdiniz!")

    baska_giris = input("Başka giriş yapmak istiyor musunuz: ").upper()

    if baska_giris == "HAYIR":

        toplam_fiyat = 0
        for urun in sepet:
            toplam_fiyat += urun["fiyat"]
        print(f"Toplam Sepet Tutarı: {toplam_fiyat} TL")
        break
    
sepet = []


def menu():
    print("<---Ürün--->")
    print("1)Tek ürün ekleme")
    print("2)Çok ürün ekleme")


def tek_urun():
    if kullanici_hangi_islem == 1:
        kullanici_urun_giris = input("Eklemek istediğiniz ürünü giriniz:")
        sepet.append(kullanici_urun_giris)
        print(sepet)
    else:
        print("Hatalı tuşlama yaptınız")


def cift_urun():
    while True:
        if kullanici_hangi_islem == 2:
            kullanici_urun = input("Eklemek istediğiniz ürünü giriniz:")
            sepet.append(kullanici_urun)
            if kullanici_urun == "q":
                break
            elif kullanici_urun == "Q":
                print(sepet)


menu()
kullanici_hangi_islem = int(input("Hangi işlemi yapıcaksınız"))

if kullanici_hangi_islem == 1:
    tek_urun()
elif kullanici_hangi_islem == 2:
    cift_urun()


sepet=[]
def menu():
     for kod, bilgi in urunler.items():
        print(f"{kod} {bilgi['ad']} {bilgi['fiyat']} ")
     print("<---Ürün--->")
     print("1)Tek ürün ekleme")
     print("2)Çok ürün ekleme")


def tek_urun():
        secim = input("Eklemek istediğiniz ürünün kodunu giriniz: ")
      
        if secim.isdigit():
            kod=int(secim)
            if kod in urunler:
                if kod in sepet:
                      print("Ürün zaten var.")
                else:
                    sepet.append(kod)
                    
            else:
                print("Hatalı giriş yaptınız")

        for kod in sepet:
            print(f"Ürün adı: {urunler[kod]['ad']} Fiyat: {urunler[kod]['fiyat']} ")
             


def cift_urun():
    while True:
            secim = input("Eklemek istediğiniz ürünün kodunu giriniz: ")
            if secim=="q":
                for kod in sepet:
                        print(f"Ürün adı: {urunler[kod]['ad']} Fiyat: {urunler[kod]['fiyat']} ")
                break
            
            if secim.isdigit():
                kod=int(secim)
                if kod in urunler:
                    if kod in sepet:
                         print("Ürün zaten var.")
                    else:
                        sepet.append(kod)
                        print(f"Ürün adı: {urunler[kod]['ad']} Fiyat: {urunler[kod]['fiyat']} ")
                else:
                    print("Hatalı giriş yaptınız")

           
           
  
menu()
islem = input("Hangi işlemi yapacaksınız: ")

if islem == "1":
    tek_urun()
elif islem == "2":
    cift_urun()
else:
    print("Hatalı tuşlama yaptınız")
