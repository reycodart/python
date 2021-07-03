# Alt ve üst limiti verilen iki sayının arasında 
# kalan ve belirli sayıya bölünebilen tüm sayıları
# gösterin.

ust_limit = int(input("Üst limiti girin: "))
alt_limit = int(input("Alt limiti girin: "))
n = int(input("Bölünebilme kontrolü yapılacak sayıyı gir: "))
print(f'{alt_limit}-{ust_limit} arasındaki {n} e/a bölünen sayı listesi:')
 
liste = []
i = alt_limit
while i <= ust_limit:
    liste.append(i)
    i += 1
    
for r in liste:
    if r % n == 0:
        print(r)

