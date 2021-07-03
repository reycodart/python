def su_hesapla(kilo):
    erkek_hesapla = kilo*0.04
    kadin_hesapla = kilo*0.03
    
    cinsiyet = input("Cinsiyet gir(kadın/erkek): ").lower()

    if cinsiyet == "erkek":
        print("-"*20)
        print(erkek_hesapla,"Litre Su İçmelisin..")
    elif not cinsiyet:
        print("Lütfen cinsiyet belirtin")

    elif cinsiyet == "kadın":
        print("-"*20)
        print(kadin_hesapla,"Litre Su İçmelisin..")

kilo_al = int(input("Kilonu gir: "))

su_hesapla(kilo_al)

