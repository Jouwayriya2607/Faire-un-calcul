taches = []    #Liste qui contient toutes les taches 


def afficher_menu():       #Affiche le menu
    print("Menu")
    print("1. Ajouter une tâche")   #Il sert à a ajouter une tache
    print("2. Modifier une tâche")   #Il sert à modifier une tache
    print("3. Supprimer une tâche")    #Il sert à supprimer une tache
    print("4. Afficher toutes les tâches")   #Il sert à affiCher toutes les taches
    print("0. Quitter")  #Il sert à quitter le programme


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche.")
        return

    for i, tache in enumerate(taches, start=1):  #Il sert à énumérer toutes les taches
        print(f"{i}. (P{tache['priorite']}) {tache['titre']} - [{tache['statut']}]")



def demander_priorite():   #Il demande aux utilisateurs les priorités des taches
    while True:
        try:
            priorite = int(input("Priorité (1 = faible, 2 = moyenne, 3 = élevée) : "))
            if 1 <= priorite <= 3:
                return priorite
            else:
                print("La priorité doit être entre 1 et 3.")
        except:
            print("Priorité invalide.")


def ajouter_tache():      #Il sert à ajouter une tache
    titre = input("Titre de la tâche : ")
    if titre == "":
        print("Le titre ne peut pas être vide.")
        return

    priorite = demander_priorite()

    tache = {
        "titre": titre,
        "priorite": priorite,
        "statut": "à faire"
    }

    taches.append(tache)   #La tache est ajoutée
    print("Tâche ajoutée.")

  
def modifier_tache():   #Il sert à modifier une tache
    if len(taches) == 0:
        print("Aucune tâche à modifier.")
        return

    afficher_taches()    #Il sert à afficher toutes les taches

    try:
        num = int(input("Numéro de la tâche à modifier : "))
        if 1 <= num <= len(taches):
            tache = taches[num - 1]

            nouveau_titre = input("Nouveau titre (Entrée pour garder) : ")
            if nouveau_titre != "":
                tache["titre"] = nouveau_titre

            choix = input("Modifier la priorité ? (o/n) : ") #Il sert à cahnger les priorités
            if choix.lower() == "o":
                tache["priorite"] = demander_priorite()

            print("Tâche modifiée.")
        else:
            print("Numéro invalide.")
    except:
        print("Saisie invalide.")


def supprimer_tache():    #Il sert à supprimer les taches
    if len(taches) == 0:
        print("Aucune tâche à supprimer.")
        return

    afficher_taches()

    try:
        num = int(input("Numéro de la tâche à supprimer : "))
        if 1 <= num <= len(taches):
            del taches[num - 1]
            print("Tâche supprimée.")
        else:
            print("Numéro invalide.")
    except:
        print("Saisie invalide.")


# Boucle principale
while True:
    afficher_menu()
    choix = input("Choix : ")

    if choix == "1":
        ajouter_tache()
    elif choix == "2":
        modifier_tache()
    elif choix == "3":
        supprimer_tache()
    elif choix == "4":
        afficher_taches()
    elif choix == "0":
        print("Au revoir.")
        break
    else:
        print("Choix invalide.")

    input("Entrée...")

