def Saisie(texte):
    valeur = input(f"Valeurs de {texte} (espacées d'un ,)")
    liste_valeur_brute = valeur.split(",")
    liste_valeur = []
    for i in liste_valeur_brute:
        liste_valeur.append(float(i))
    return liste_valeur