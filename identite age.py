def afficher_identite(prenom, nom, age):
    print("Bonjour " + prenom + " " + nom + ", tu as " + str(age) + " ans.")
    print("L'an prochain tu auras " + str(age + 1) + " ans.")

    # majorité / minorité
    if age >= 18:                      #Si vous avez plus de 18 ans
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")      #Sinon 


# Programme principal
prenom = input("Entrez votre prénom : ")      #Demander d'entrer un prénom
nom = input("Entrez votre nom : ")            #Demander d'entrer un nom
age = int(input("Entrez votre âge : "))        #Demander l'age

afficher_identite(prenom, nom, age)          #Affichage du prenom, nom et age de l'utilisateur
