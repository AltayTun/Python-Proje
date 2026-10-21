
#Firmamız
transfer={
    "EFT",
    "FAST",
    "Havale"
}
#Rakip firma
transfer2={
    "EFT",
    "Kripto",
    "SWIFT"
}
ortak=transfer&transfer2
print(f"İşlemler".center(20,"-"))
print(f"Ortak transfer şekiller:{ortak}")
firma=transfer-transfer2
print(f"Bizim Transfer şekillerimiz:{firma}")
musteri_transfer=input("Lütfen transfer yapamk istediğiniz şekli giriniz:")
bakiye=float(input("Lütfen bakiyenizi giriniz:"))
dogum=int(input("Lütfen doğduğunuz yılı giriniz:"))
bloke=input("Hesabınız donduruldumu?")
bakiye_cekimi=float(input("Çekmek istediğiniz tutarı giriniz"))

b=bloke.upper().strip()
blok=b=="EVET"or b=="evet"
print(f"Hesap bloke durmunuz:{blok}")

yas=2026-dogum>=18
print(f"Para çekme yaş durumunuz:{yas}")

cekim= bakiye>=bakiye_cekimi
print(f"Bakiye çekilme durumu:{cekim}")

kontrol=transfer==musteri_transfer 
print(f"Transfer biçiminiz:{bool(kontrol)}")

