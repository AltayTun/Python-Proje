urun_listesi=[]
urunler={
    "İSKENDER":{
        "Stok durumu":10,
        "Fiyat":200
    },
    "HAMBURGER":{
        "Stok durumu":5,
        "Fiyat":300
    },
    "PİZZA":{
        "Stok durumu":0,
        "Fiyat":150
    },
    "MAKARNA":{
        "Stok durumu":0,
        "Fiyat":100
    }
    
}
sepet={}
def vergiHesabı():
    pass

def urun_ekleme():

    if urunAd==stok_kontrol():
        yeni_urun_ekleme=urun_listesi.append()
    else:
        urunAd=input("Eklemek üstediğiniz ürün sepette yok lütfen başka ürün giriniz:").upper()
    return

def stok_kontrol():
    if urunler[urunAd]["Stok durumu"]>0:
        return True
    else:
        return False

print("<---------Ürün Sepeti---------->")
urunAd=input("Sepete eklemek istediğiniz ürün adını giriniz:").upper()
if urunAd not in urunler:
    urunAd=input("Girdiğiniz ürün yok lütfen mağazamızda bulunan bir ürün giriniz:").upper()


if stok_kontrol()==False:
    urunAd=input("Girdiğiniz ürün stokta yok lütfen başka ürün giriniz:").upper()
else:
    urun_ekleme()
    print(urun_listesi)



    