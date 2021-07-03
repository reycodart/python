
sayi = int(input("Sayı gir: "))
gecici = sayi
ters = 0

while (sayi > 0):
    son_basamak = sayi % 10
    ters = ters * 10 + son_basamak
    sayi = sayi // 1011

if gecici == ters:
    print("Palindrom sayıdır..")
else:
    print("Palindrom sayı değildir..")

