#Kahve Dükkanı kasası
"""
{
kahveler
}
Kahv giriş kullanıcı
if kahve giris not in kahveler 
{
0HATA0!!
}
elif kahve giris in kahveler
{
kaç adet kullanıcı
toplam odenecek tutar
}

"""
kahveler={
"ESPRESSO":{
    "fiyat":80 
        },
"LATTE":{
    "fiyat":100
},
"ÇAY":{
    "fiyat":30
}
}

kahve_secimi=input("Lütfen listeden kahve seçiniz: ").upper()

if kahve_secimi not in kahveler:
    kahve_secimi=input("Seçtiğiniz ürün listede yok || Lütfen listeden kahve seçiniz: ").upper()
    if kahve_secimi in kahveler:
        adet=int(input("Seçtiğiniz kahveden kaç adet istersini?"))
        toplam=kahveler[kahve_secimi]["fiyat"]*adet
        print(f"Toplam borcunuz {toplam} ")
elif kahve_secimi in kahveler:
    adet=int(input("Seçtiğiniz kahveden kaç adet istersini?"))
    toplam=kahveler[kahve_secimi]["fiyat"]*adet
    print(f"Toplam borcunuz {toplam} ")


#Güvenlik şifresi doğrulayıcı
"""
Yeni Şifre gir kulanıcı giris
if lenKUl==8 olacak 
{
if and "@","#"in Kul olacak:
{
Şifr onaynlandı
{
hata
}
}

}
else:
hata

"""
yeni_sifre=input("Yeni şifrenizi giriniz:")

if len(yeni_sifre)>8 or len(yeni_sifre)<8:
    yeni_sifre=input("Karakter sayınızı uyumsuz || Yeni şifrenizi giriniz:")
    if len(yeni_sifre)==8:
        if "@" in yeni_sifre or "#" in yeni_sifre:
            print("Şifreniz onaylandı")
        else:
            print("'@'veya'#' kullanılmalı ||Şifreniz onaylanmadı.")
elif len(yeni_sifre)==8:
    if "@" in yeni_sifre or "#" in yeni_sifre:
        print("Şifreniz onaylandı")
    else:
        print("'@'veya'#' kullanılmalı || Şifreniz onaylanmadı.")


#Basit Not hesaplayıcı:
"""
vize
final
(vize*0.40)+final0.60/2
if ort 50>ort
gecti
else
kaldı

"""
vize=int(input("Vize giriniz:"))
final=int(input("Fİnal giriniz:"))
ortalama=((vize*0.40)+(final*0.60))/2
if ortalama>50:
    print("Geçti")
else:
    print("Kaldı")