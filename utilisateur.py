import json

#Enregistre un nouvel utilisateur dans le fichier users.json
def save_user(user):
    with open("users.json", "r") as f:
        users= json.load(f)
        users.append(user)
        
    with open('users.json', 'w') as file:
        user_json = json.dumps(users)
        file.write(user_json)
        
#Crée un nouvel utilisateur en demandant les informations à l'utilisateur
def create_user():
       with open("users.json", "r") as f:
        users = json.load(f)
        if len(users) == 0:
            idUser = 1
        else:
            idUser = users[-1]["id"] + 1
        name = input("Entrer le nom du lecteur : ")
        email = input("Entrer l'email du lecteur : ")
       
        if  not name or not email  :
            print("veuillez remplir tous les champs")
            return
        elif  name.startswith(("#", "@", "$", "%", "&", "_ ")) : 
            print("que le nom ne commence pas avec des caracteres speciaux")
            return
       
        user = {
        'id': idUser,
        'name': name,
        'email': email,
        }

        save_user(user)
        
'''Affiche tous les utilisateurs dans le fichier users.json en lisant le fichier, en vérifiant si il est vide,
puis en imprimant les détails de chaque utilisateur'''       
def show_all_users(): 
    try:
        with open("users.json", "r") as f:
            users = json.load(f)
            if len(users) == 0:
                print("Le fichier JSON est vide.")
            else:
                for user in users:
                    print("voici la liste de tous vos lecteurs")
                    print("-----------------------------------")
                    print(f"\t lecteur ID: {user['id']}")
                    print(f"\t nom du lecteur: {user['name']}")
                    print(f"\t email: {user['email']}")

    except FileNotFoundError:
        print("Le fichier JSON n'existe pas.")
    except json.JSONDecodeError:
        print("Le fichier JSON est mal formaté.")
def deleteUser():
    user = int(input("Entrez l'ID du lecteur à supprimer: "))
    with open("users.json", "r") as f:
        users = json.load(f)
    index = -1 
    for i in range(len(users)):
        if users[i]["id"] == user:
            index = i
            break
    if index != -1:
        del users[index]
        with open("users.json", "w") as f:
            json.dump(users, f)
        print("le lecteur a été supprimé.")
    else:
        print("le lecteur non trouvé !.")
        print("le lecteur non trouver !.")
    
def choice_to_manage_users():
    print("1. afficher tous les lecteurs ")
    print("2. ajouter un lecteur")
    print("3. suprimer un lecteur")
    choice = int(input("selectionez une optiion : "))
    return choice
        
#Affiche un menu pour gérer les fonctions des utilisateurs
def manage_users(): 
    choice = choice_to_manage_users()
    if choice == 1: 
       show_all_users()
    elif choice == 2: 
        create_user()
    elif choice == 3 :
        deleteUser()
        


