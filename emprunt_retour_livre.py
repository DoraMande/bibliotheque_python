import json
def emprunter_livre():
    with open("livres.json", "r") as f:
        livres = json.load(f)
    livre_id = int(input("Entrez l'ID du livre à emprunter: "))
    for livre in livres:
        if livre["id"] == livre_id:
            if livre.get("Disponible", True):
                livre["Disponible"] = False
                with open("livres.json", "w") as f:
                    json.dump(livres, f)
                print("Livre emprunté avec succès.")
            else:
                print("Le livre n'est pas disponible.")
            return
    print("Livre non trouvé.")

def retourner_livre():
    with open("livres.json", "r") as f:
        livres = json.load(f)
    livre_id = int(input("Entrez l'ID du livre à retourner: "))
    for livre in livres:
        if livre["id"] == livre_id:
            if not livre.get("Disponible", True):
                livre["Disponible"] = True
                with open("/home/jonathanbolibenga/Documents/project python bibliotheque/livres.json", "w") as f:
                    json.dump(livres, f)
                print("Livre retourné avec succès.")
            else:
                print("Le livre est déjà disponible.")
            return
    print("Livre non trouvé.")