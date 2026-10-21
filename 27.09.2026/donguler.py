#1
negatif_sayi=[-5, 3, -8, 12, -1, 7]
pozitif_liste=[]
for sayi in negatif_sayi:
    if sayi<0:
        pozitif_liste.append(sayi*-1)
    else:
        pozitif_liste.append(sayi)
print(f"Yeni liste {pozitif_liste}")

#2
sesli_harf=["a", "e", "ı", "i", "o", "ö", "u", "ü"]
giris=input("Kelime giriniz:").lower()
sayac=0
for harf in giris:
    if harf in sesli_harf:
        sayac+=1
print(f"Toplam sesli harf sayısı:{sayac}")


#3
toplam = 0
adet = 0
while True:
    sayi = int(input("Sayı giriniz (Çıkmak ve hesaplamak için 0): "))
    if sayi == 0:
        break
    toplam += sayi
    adet += 1  # Ortalamayı bulabilmek için kaç sayı girildiğini sayıyoruz

if adet > 0:
    ortalama = toplam / adet
    print(f"Toplam: {toplam} | Ortalama: {ortalama}")
else:
    print("Hiç sayı girilmedi.")

#4
tahmin=42


kullanici_tahmin=int(input("Sayı tutuldu Tahminini giriniz:"))

while kullanici_tahmin!=tahmin:
    if kullanici_tahmin<tahmin:
        kullanici_tahmin=int(input(f"Önceki tahmininz:{kullanici_tahmin} || YUKARI:"))
    elif kullanici_tahmin>tahmin:
        kullanici_tahmin=int(input(f"Önceki tahmininz:{kullanici_tahmin} || AŞAĞI:"))
        
        
print(f"GİRİŞ BAŞARILI:{tahmin}")

#5
liste1 = [1, 3, 5, 7, 9]
liste2 = [2, 3, 6, 7, 10]
ortak_liste=[]

for eleman in liste1:
    if eleman in liste2:
        ortak_liste.append(eleman)
print("Ortak sayılar:",ortak_liste)

#Başka yöntem olarak
#set(liste1)&set(liste2)
        
#6

kelimeler=["python", "akış", "döngü", "algoritma", "kod", "geliştirici"]
for kelime in kelimeler:
    if len(kelime)>5:
        print(f"Kelime:{kelime} || Kelime sayısı:{len(kelime)}"),

#7
kullanici_giris=input("Kelime giriniz:")
benzersiz_harfler = set(kullanici_giris)
for harf in benzersiz_harfler:
    sayac=kullanici_giris.count(harf)
    print(f"{harf}:{sayac}")
    
        

#8
for i in range(5,0,-1):
    print("*"*i)

#9
a=0
b=1
print("Fibonacci Serisi:")

for _ in range(15):
    print(a,end=" ")
    a,b=b,a+b

#10
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
kosegen_toplami = 0
for i in range(len(matris)):
    kosegen_toplami += matris[i][i]
print(f"Köşegen Elemanların toplamı:{kosegen_toplami}")





        



