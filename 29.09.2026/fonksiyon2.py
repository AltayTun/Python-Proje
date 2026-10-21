#1
def indirimli_fiyat(fiyat,indirim_yuzdesi):
    indirim=fiyat*(indirim_yuzdesi/100)
    son_fiyat=fiyat-indirim
    return son_fiyat
print(indirimli_fiyat(1000,2))

#2
def ortalama_hesapla(*notlar):
    toplam = 0
    for n in notlar:
        toplam += n  
    
    ortalama = toplam / len(notlar)  
    return ortalama
print(ortalama_hesapla(70, 80, 90)) 
#3
def zam_hesapla(**calisanlar):
    zam_orani = 0.20
    for isim,mevcut_maas in calisanlar.items():
        zamli_maas=mevcut_maas+(mevcut_maas*zam_orani)
        print(f"Zamn öncesi: {isim}:{mevcut_maas} || Zam sonrası: {isim}:{zamli_maas}")

zam_hesapla(emre=1000,ayse=12000)

#4
def kritik_stok_bul(urun_stoklari,kritik_limit):
    kritik_urunler=[]
    for urun,stok in urun_stoklari.items():
        if stok<kritik_limit:
            kritik_urunler.append(urun)
    return kritik_urunler
stoklar={"Elma": 15, "Armut": 5, "Muz": 2}
print(kritik_stok_bul(stoklar, 10))

#5



    