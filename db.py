from pytube import YouTube
import time

def bilgileri_goster():
    url = YouTube(input("Görmek istediğin linki yapıştır: "))
    son_dakika = url.length/60
    print("-"*30)
    print("Video başlığı:", url.title)
    print("Video sahibi:",url.author)
    print("Videonun küçük resmi:", url.thumbnail_url)
    print("İzlenme sayısı:", url.views)
    print("Video uzunluğu:", son_dakika,"dk")
    print("-"*30)
#-------------------------------------------------------------
def video_indir():
    url = YouTube(input("Link: "))
    indirme_baglantisi = url.streams.filter(res="144p",mime_type="video/mp4").first()
    son_dakika = url.length/60
    indirme_baglantisi.download()
    print("-"*30)
    print("Video başlığı:", url.title)
    print("Video sahibi:",url.author)
    print("İzlenme sayısı:", url.views)
    print("Video uzunluğu:", son_dakika,"dk")
    print("-"*30)
#video_indir()

#---------------------------------------------------ses indirme:

def ses_indir():
    url = YouTube(input("Link: "))
    indirme_baglantisi = url.streams.filter(mime_type="audio/mp4").first()
    son_dakika = url.length/60
    indirme_baglantisi.download()
    print("-"*30)
    print("Ses başlığı:", url.title)
    print("Sesin sahibi:",url.author)
    print("İzlenme sayısı:", url.views)
    print("Ses uzunluğu:", son_dakika,"dk")
    print("-"*30)


while True:
    sec = input("1-YouTube Video Bilgilerini Göster\n2-Video İndir\n3-Ses İndir\n4-Çıkış\n")
    if sec=="1":
        bilgileri_goster()
        input("Devam edilsin mi?")#Devam için ENTER a bas..
    elif sec == "2":
        video_indir()
        input(input("Devam edilsin mi?"))
    elif sec == "3":
        ses_indir()
    else:
        print("Çıkış yapılıyor..")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Uygulamadan çıktınız..")
        break





