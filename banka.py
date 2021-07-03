def para_cek(users, cusNo):
    amount = input("Miktar giriniz: ")
    if users[cusNo]["balanca"] > amount:
        print(amount, "Tl'niz hazır")
        users[cusNo]["balance"] -= amount
    else:
        print("paran yetmediii")


def para_gonder(users, cusNo):
    sendNo = input("Hangi hesaba göndericeksin? ")
    amount = int(input("Miktarını gir: "))
    if users[cusNo]["balance"] > amount:
        print("Paran gönderiliyor.")
        users[cusNo]["balance"] -= amount
        users[sendNo]["balance"] += amount
    else:
        print("Paran yetersiiiz")


def giris(users, cusNo):
    print("Giriş başarılı")
    opt = input("İşlem seç lütfen: 1-Para Çek 2-Para Gönder: ")
    if int(opt) == 1:
        para_cek(users, cusNo)
    elif int(opt) == 2:
        para_gonder(users, cusNo)


users = {"123":{"name":"Ahmet", "password":"abc", "balance":200000000},
"124":{"name":"mithat", "password":"abcd", "balance":3000}}

print("Bankamıza Hoşgeldiniz (:")
cusNo = input("Müşteri numaranızı girin: ")
cusPw = input("Şifrenizi girin: ")

if cusNo not in users:
    print("Böyle bir kullanıcı bulunamadı :(")
else:
    if cusPw == users[cusNo]["password"]:
        giris(users, cusNo)
    else:
        print("Bilgiler hatalı giriş başarısız.")

print(users)

