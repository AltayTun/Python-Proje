# for i in range(0,51,2):
#     print(i)


# sifre="python123"
# kullanici_sifre=input("Lütfen şifrenizi giriniz:")

# while kullanici_sifre!=sifre:
#     kullanici_sifre=input("GİRDİĞİNİZ ŞİFRE HATALI!!Lütfen şifrenizi giriniz:")
# print("Giriş başarılı")

# for i in range(1,11):
#     if i==5:
#         continue
#     print(list[i])


# while True:
#     kullanici = input("Yazın (Çıkmak için 'cikis' yazın): ")
#     if kullanici == "cikis":
#         print("Döngüden çıkıldı.")
#         break
#     print(f"Yazdığınız: {kullanici}")


# meyveler = ["Elma", "Armut", "Muz", "Çilek"]

# for index,meyve in enumerate(meyveler):
#     print(f"Sıra numarası:{index} Meyve:{meyve}")

sayilar = [10, 20, 10, 30, 20, 40, 50, 30, 10]
index=0
for sayi in sorted(set(sayilar)):
    index+=1
    print(f"Sıra:{index} Sayı:{sayi}",end=" ")