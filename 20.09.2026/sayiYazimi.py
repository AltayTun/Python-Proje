#1 den 10 a kadar olan sayıların kareleri yazımı
x=0
while x<= 10:
    print(x*x)
    x+=1
#for ile
for x in range(11):
    print(x*x)

#Kullanıcı doğru şifre girimi
sifre=1234
sayi1=int(input("Şifre giriniz:"))

while sayi1!=sifre:
    print("Lütfen tekrar deneyiniz")
    sayi1=int(input("Şifre giriniz:"))
print("Şifreniz doğru")

#Ürünler yazdırımı
urunler=[
    {"Ürün Adı:":"Kayısı","Fiyat":"45"},
    {"Ürün Adı:":"Şeftali","Fiyat":"55"},
    {"Ürün Adı:":"Portakal","Fiyat":"35"},
    {"Ürün Adı:":"Üzüm","Fiyat":"75"}
]
for urun in urunler:
    print(urun)


#Sınırsız değer girme sayı tutma
toplam=0
sayi=1
giris=int(input(f"{sayi}.sayıyı giriniz:"))
while giris!=0:
    toplam+=giris
    print(f"Güncel Toplam: {toplam}")
    sayi+=1
    giris=int(input(f"{sayi}.sayıyı giriniz:"))
print(f"İşlem bitti! Son Toplam: {toplam}")
    
