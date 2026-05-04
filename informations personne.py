"""Premier programme
Formation Python
apprendre la programmation"""
prenom = input("Quel est ton prénom")
nom = input("Quel est ton nom ?")
age = input("Quel est ton age ?")

try:
    age_int = int(age)
except ValueError:
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    print("Je m'appelle" + nom + ", j'ai " + str(age_int) + " ans")
    print("L'an prochain vous aurez " + str(age_int + 1) + "ans")

    #Déclaration de la fonction
    def afficher_informations_personne(nom, age, ville):
        print("Je m'appelle" + nom + ", J'ai" + str(age)+ " ans")
        print("J'habite à " + ville)
        print("L'an prochain j'ai" + str(age + 1) + " ans")
        print("Cela représente environ" + str(age * 12) + "mois de vie")
