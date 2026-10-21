#1
# for i in range(1,21):
#     print(i)
#2
sayac=10
while sayac>=1:
    if sayac==0:
        sayac -=1
print("Süreniz bitti.")

#3
sayilar=[5, 12, 8, 3, 20]
toplam =0
for sayi in sayilar:
    toplam+=sayi
print(toplam)

#4
# giris=input("Lütfen bir kelime giriniz:")

# for index,i in enumerate(giris):
#     print(f"Sıra:{index} Harf:{i}")

#5
while True:
    girdi = input("Bir şey yazın (Durmak için 'dur' yazın): ")
    if girdi.lower() == "dur":
        print("Giriş başarılı")
        break
#6
sayi = int(input("Sayı giriniz: "))
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
#7
for i in range(1, 31):
    if i % 3 == 0:
        continue  
    print(i)
#8
sayi = [4, 1, 7, 4, 2, 1, 9, 2]
print(sorted(set(sayi)), sep=", ")
#9
for i in range(1, 6):
    print("*" * i)  

#10

kullanici_sayi = int(input("Sayı giriniz: "))

is_asal = True

if kullanici_sayi < 2:
    is_asal = False
else:
    for i in range(2, kullanici_sayi):
        if kullanici_sayi % i == 0:  # Kendinden küçük başka bir sayıya tam bölündü mü?
            is_asal = False
            break  # Bölündüyse asal değildir, döngüyü bitir

if is_asal:
    print(f"{kullanici_sayi} bir asal sayıdır.")
else:
    print(f"{kullanici_sayi} bir asal sayı değildir.")

