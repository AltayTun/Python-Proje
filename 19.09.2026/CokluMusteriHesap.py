key=int(input("Müşteri anahtarını giriniz:"))
musteri_ad=input("Müşteri adını giriniz:")
bakiye=float(input("Müşterinin bakiyesini giriniz:"))
uyelik=input("Müşteri Üyelik durumunu giriniz:")
x=uyelik.upper().strip()
yeni_uyelik=x=="VİP" or x=="VIP"

musteri={
    key:{
        "Müşteri Adı":musteri_ad,
        "Bakiye":bakiye,
        "Vip Üyelik Durumu":yeni_uyelik
    }
}
print(f"Müşteri bilgileri".center(30,"-"))
print(musteri)