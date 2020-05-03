"""Un programme en python pour tester l'outil GitHub Actions"""

def pythagore(cote_a, cote_b, cote_c):
    """Théorème de pythagore"""

    # On vérifie que l'hypoténuse est plus grand que les deux autres côtés
    assert isinstance(cote_a, float), "Mauvais typage pour a"
    assert isinstance(cote_b, float), "Mauvais typage pour b"
    assert isinstance(cote_c, float), "Mauvais typage pour c"
    assert cote_a > cote_b and cote_a > cote_c, "Hypoténuse mauvais"

    somme_carre = (cote_c ** 2 + cote_b ** 2)
    rectangle = bool((cote_a ** 2) == somme_carre)
    return rectangle

if __name__ == '__main__':
    HYPOTENUSE = float(input("Hypoténuse : "))
    COTE_2 = float(input("Rentrez la valeur du deuxième côté : "))
    COTE_3 = float(input("Rentrez la valeur du dernier côté : "))

    EST_CARRE = pythagore(HYPOTENUSE, COTE_2, COTE_3)
    print(f"Triangle rectangle : {EST_CARRE}")
