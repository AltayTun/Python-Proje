sayi = int(input("Sayı giriniz"))

match sayi:
    case x if x > 0:
        print("Pozitif sayı:")
    case x if x < 0:
        print("Negatif sayı:")
    case _:
        print("Sıfır")