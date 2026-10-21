kullanici_listesi = {
    "emre": {"sifre": "1234", 
             "email": "emre@gmail.com"
            },
    "ahmet": {"sifre": "5678",
             "email": "ahmet@gmail.com"
             }
}

print("--- KULLANICI GİRİŞ VE KAYIT SİSTEMİ ---")

while True:
    kullanici_ad = input("Kullanıcı adını giriniz (Çıkış için 'q' yazın): ").lower()
    if kullanici_ad == 'q':
        print("Sistemden çıkılıyor. İyi günler!")
        break
        
    sifre = input("Şifrenizi giriniz: ")
    
   
    if kullanici_ad in kullanici_listesi:
        if sifre == kullanici_listesi[kullanici_ad]["sifre"]:
            print(f"Hoş geldin, {kullanici_ad}!")
            break  
        else:
            print("Hata: Şifre yanlış! Tekrar deneyin.")
            
    
    else:
        cevap = input("Listede isminiz yok. Listeye eklemek ister misiniz? (EVET/HAYIR): ").upper()
        
        if cevap == "EVET":
            email = input("Email adresinizi giriniz: ")
            
           
            kullanici_listesi[kullanici_ad] = {
                "sifre": sifre,
                "email": email
            }
            print(f"Başarılı: '{kullanici_ad}' sisteme eklendi!")
            print("Güncel Veri Tabanı:", kullanici_listesi)
            break
        else:
            print("İşlem iptal edildi, tekrar deneyebilirsiniz.")