# 1. Adım: ARABA KALIBINI (Class) Yaratıyoruz
class Araba:
    # __init__ bizim yapıcı metotumuzdur (Fabrikada üretilirken ilk çalışan ayarlar)
    def __init__(self, marka, model, renk):
        self.marka = marka  # Özellik (Attribute)
        self.model = model  # Özellik (Attribute)
        self.renk = renk    # Özellik (Attribute)
        self.hiz = 0        # Başlangıçta hızımız sıfır

    # Davranış / Metot (Method)
    def gaz_ver(self, miktar):
        self.hiz += miktar
        print(f"{self.renk} renkli {self.marka} hızlandı! Şu anki hız: {self.hiz} km/s")

    def fren_yap(self, miktar):
        self.hiz -= miktar
        if self.hiz < 0:
            self.hiz = 0
        print(f"{self.marka} yavaşladı. Şu anki hız: {self.hiz} km/s")

# 2. Adım: Bu kalıptan ARABALAR (Nesneler) Üretiyoruz
araba1 = Araba("Toyota", "Corolla", "Beyaz")
araba2 = Araba("BMW", "3.20", "Siyah")

# 3. Adım: Arabaları harekete geçiriyoruz!
araba1.gaz_ver(50)   # Çıktı: Beyaz renkli Toyota hızlandı! Şu anki hız: 50 km/s
araba2.gaz_ver(100)  # Çıktı: Siyah renkli BMW hızlandı! Şu anki hız: 100 km/s

araba1.fren_yap(20)  # Çıktı: Toyota yavaşladı. Şu anki hız: 30 km/s