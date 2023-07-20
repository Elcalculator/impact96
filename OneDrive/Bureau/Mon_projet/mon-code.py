# Ceci est un programme Python pour calculer la factorielle d'un nombre entier positif

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

nombre = int(input("Entrez un nombre entier positif : "))

if nombre < 0:
    print("Erreur : Le nombre doit être positif.")
else:
    resultat = factorielle(nombre)
    print(f"La factorielle de {nombre} est : {resultat}")
