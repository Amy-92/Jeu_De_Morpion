import random

#Tableau de jeu
grille = [" " for _ in range(9)]

#Fonction pour afficher le tableau
def afficher_grille():
    print(f" {grille[0]} | {grille[1]} | {grille[2]}")
    print("---+---+---")
    print(f" {grille[3]} | {grille[4]} | {grille[5]}")
    print("---+---+---")
    print(f" {grille[6]} | {grille[7]} | {grille[8]}")

#Fonction pour vérifier si un joueur a gagné
def verifier_gagne(joueur):
    # Vérifier les lignes
    for i in range(3):
        if grille[i*3] == joueur and grille[i*3+1] == joueur and grille[i*3+2] == joueur:
            return True
    # Vérifier les colonnes
    for i in range(3):
        if grille[i] == joueur and grille[i+3] == joueur and grille[i+6] == joueur:
            return True
    # Vérifier les diagonales
    if grille[0] == joueur and grille[4] == joueur and grille[8] == joueur:
        return True
    if grille[2] == joueur and grille[4] == joueur and grille[6] == joueur:
        return True
    return False

#Fonction pour jouer un coup
def jouer_coup(joueur, coup):
    if grille[coup] != " ":
        print("Coup invalide, case déjà occupée.")
        return
    grille[coup] = joueur
    if verifier_gagne(joueur):
        print(f"Joueur {joueur} a gagné!")
        afficher_grille()
        return True
    return False

#Fonction pour jouer un coup aléatoire pour l'ordinateur
def jouer_coup_ordi():
    coup = random.randint(0, 8)
    while grille[coup] != " ":
        coup = random.randint(0, 8)
    jouer_coup("O", coup)

#Boucle de jeu
while True:
    afficher_grille()
    coup = input("Joueur X, entrez votre coup (1-9) : ")
    if jouer_coup("X", int(coup)-1):
        break
    jouer_coup_ordi()
    if verifier_gagne("O"):
        afficher_grille()
        print("L'ordinateur a gagné!")
        break