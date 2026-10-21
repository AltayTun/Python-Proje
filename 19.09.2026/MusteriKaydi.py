ad=input("Adınızı giriniz:")
soyad=input("Soyadınızı giriniz:")
tc=input("TC no giriniz:")
bakiye=float(input("Bakiyenizi giriniz:"))
yas=int(input("Yaşınızı giriniz:"))
duzgun_ad=ad.strip().capitalize()
duzgun_soy=soyad.strip().capitalize()
duzgun_tc=len(tc)==11

print(f"Adınız:{duzgun_ad}\nSoyadınız:{duzgun_soy}\nTC numaranız:{duzgun_tc}\nBakiyeniz{bakiye}\nYaşınız:{yas}")