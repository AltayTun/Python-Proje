#1

kup=lambda x:x**3
print(kup(5))

#2

yarim=lambda x,y:(x+y)//2
print(yarim(10,10))

#3
sayilar=[2,4,6,8]

carpim=list(map(lambda x:x**3,sayilar))
print(carpim)

#4
liste=["merhaba","python","dünya"]

unlem=list(map(lambda x:x+"!",liste))
print(unlem)
#5
sayi=[1, 2, 3, 4, 5, 6, 7, 8]

secim=list(filter(lambda x:x%2>=1 ,sayi))
print(secim)

#6
meyve=["elma", "armut", "muz", "karpuz", "ananas"]

a_harfi=list(filter(lambda x:"a" in x,meyve))
print(a_harfi)

#7
fahrenheit=[32, 68, 104]
donusum=list(map(lambda x:(x-32)*5/9,fahrenheit))
print(donusum)

#8
sayilar=[10, 55, 30, 80, 45, 90, 20]
filtreleme=list(filter(lambda x:x>50,sayilar))
print(sayilar)

#9
sayilar=[1, 2, 3, 4, 5, 6]
cift=list(filter(lambda x:x%2==0,sayilar))
kare=list(map(lambda x:x**2,cift))
print(kare)

#10
yazi=["kod", "python", "ai", "yazilim", "git"]
karakter=list(filter(lambda x:len(x)>3,yazi))
buyuk=list(map(lambda x:x.upper(),karakter))
print(buyuk)