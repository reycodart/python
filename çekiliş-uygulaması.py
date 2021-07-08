import random
import time

kullanicilar = list()


def kullanici_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz")
    ekle = input("Eklenecek kullanıcıyı yazın: ")
    kullanicilar.append(ekle)
    input("Devam etmek için ENTER a basınız..")

def kullanici_gor(x):
    say = 1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı Adı: ", i)
        say=+1
    print("-"*30)
    input("Devam etmek için ENTER a basınız..")

def sec(x):
    print("-"*30)
    say = 1
    kisi_sec = int(input("Kaç kişi seçilsin: "))
    rastgele_sec = random.sample(x,kisi_sec)

    for i in rastgele_sec:
        print(str(say)+"-Kullanıcı Adı: ",i)
        say =+ 1
        print("Diğer kişi sistemden çekiliyor...")
        time.sleep(2)
    print("-"*30)
    input("Devam etmek için ENTER a basınız..")

def salla(x):
    print("-"*30)
    say = 1
    random.shuffle(x)#liste içindeki sıralamayı karıştırır.

    for i in x:
        print(str(say)+"-Kullanıcı Adı: ",i)
        say =+ 1
        print("-"*30)
        input("Devam etmek için ENTER a basınız..")


while True:

    print("****ÇEKİLİŞ UYGULAMASINA OJGELDİNİZ****")
    secim = int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n"))

    if secim == 1:
        kullanici_ekle(kullanicilar)
    elif secim == 2:
        kullanici_gor(kullanicilar)
    elif secim == 3:
        salla(kullanicilar)
    elif secim == 4:
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(2)
        sec(kullanicilar)
    else:
        print("uygun bir tercih yapmalısın..")

