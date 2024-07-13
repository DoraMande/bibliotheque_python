#PAR KAHINDO YUMBA JENNIFER

from livre import ajouterLivre, aficher_livres, rechercherLivre , suprimer_ou_archiver
from utilisateur import manage_users

from emprunt_retour_livre import emprunter_livre, retourner_livre

def menu_principal():
    print("1. ajouter un livre \n")
    print("2. Rechercher un livre \n")
    print("3. suprimer un livre \n")
    print("4. Afficher le livre \n") 
    print("5. Emprunter un livre \n")
    print("6. Retournez un livre \n")
    print("7. Ajouter un nouveu utilisateur")
    print("8. Quiter \n")
    choix = int(input("selectionez une option : "))
    return choix
    
def main (): 
    while True:
        choix = menu_principal()
        if choix == 1: 
            ajouterLivre()
        elif choix == 2: 
            rechercherLivre()
        elif choix == 3: 
            suprimer_ou_archiver()
        elif choix == 4: 
            aficher_livres()
        elif choix == 5: 
            emprunter_livre()
        elif choix == 6: 
            retourner_livre()
        elif choix == 7 : 
           manage_users()
        elif choix ==  8:
            break 
            
        
if __name__ == "__main__":
    main()
