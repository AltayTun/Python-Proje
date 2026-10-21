def cay_getir(seker_sayisi=0):
    if seker_sayisi==0:
        print("Afiyet olsun! Şekersiz çayınız hazır.")
    else:
        print(f"Afiyet olsun! {seker_sayisi} şekerli çayınız hazır.")

cay_getir(3)
cay_getir()

print("*"*5)

def kargolari_al(*kargolar):
    print(f"Hasan: Patron bana toplam:{len(kargolar)} parça eşya verdin.")
    for esya in kargolar:
        print(f"Hasan taşıyor:{esya}")

kargolari_al("Dosya")

kargolari_al("Laptop","Klavye","Bant","Makas")

print("*"*5)

def dosyala(**bilgiler):
    print("Zeynep:Patron,veridiklerini çekmeceye şöyle dizdim:")
    for etiket,deger in bilgiler.items():
        print(f"- {etiket} dosyasına {deger} yazıldı.")
dosyala(isim="Ali",yas=25)

dosyala(isim="Ayşe",sehir="İzmir",meslek="Mühendis", maas=50000)

print("*"*5)

sirket_adi="Yıldız Holding"

def ahmetin_odasi():
    print(f"Ahmet: Ben {sirket_adi} şirketinde çalışıyorum.")

    gizli_kasa_sifresi="1234"
    print("Ahmet: Kasa şifresi benim odamda, güvende.")
def zeynepin_odasi():
    print(f"Zeynep: Ben de {sirket_adi} şirketinde çalışıyorum.")

ahmetin_odasi()
zeynepin_odasi()


def ahmetin_ana_gorevi(net_maas):
    def vergi_hesapla(ucret):
        return ucret * 0.15
    kesinti= vergi_hesapla(net_maas)

    odenek=net_maas - kesinti
    print(f"Ahmet:Vergi düşüldü, ödenecek net tutar: {odenek}TL")
    return odenek

ahmetin_ana_gorevi(20000)


    