def carach(nb_ch):
    if nb_ch == "":
        return 0
    else:
        return 1 + carach(nb_ch[1:])
    

nb_ch = input("Votre chaîne : ")
result = carach(nb_ch)
print("Votre chaine a pour longueur : ",result ,"caractères")

