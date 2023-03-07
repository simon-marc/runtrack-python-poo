def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)
    

n = int(input("Entrez votre nombre entier : "))
result = factoriel(n)
print("Le resultat est : ",result)
