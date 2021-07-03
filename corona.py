ates_durumu = float(input("Ateşin kaç derece?: "))
oksuruk = input("Öksürüğünüz var mı? E/H: ").lower()
bas_agrisi = input("Baş ağrınız var mı? E/H: ").lower()
gun = int(input("Şikayetleriniz kaç gündür var?: "))

if ates_durumu>=39:
    if gun >=3:
        print("UYARI -> Acilen hastaneye git!")
    else:
        print("Ateş durumu sınırda, devam ederse hastaneye git..")

if (ates_durumu>=39) and (oksuruk=="e") and (bas_agrisi=="e") and (gun>=3):
    print("Tüm semptomlar var.Kimseye yaklaşma, doktora git!")
    
elif (oksuruk=="e") or (bas_agrisi=="e") or (gun>=3):
    print("Durumun bu şekil devam ederse doktora git..")

else:
    print("Ateşin 39 u geçerse doktora git lütfen..")
    print(f"Ateşin {ates_durumu} derece.")


    