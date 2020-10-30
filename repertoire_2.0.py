import random
import os
import pickle 


print(os.getcwd())
os.chdir("C:\\Users\\admin\\Desktop\\repertoire_2.0")
fichier = open("repertoire.txt", encoding='utf-8' , mode="r")
# fichier.close();
listeMots = []
listeTirage = []
motCourant = ""


class Mot: 
    def __init__ (soi, russe, francais, coef=1, desc=""):
        soi.russe = russe
        soi.francais = francais
        soi.coef = coef
        soi.desc = desc


class Mot_jouable(Mot):
    def __init__ (soi, russe, francais, id, coef=1, desc=""):
        soi.id = id
        Mot.__init__(soi, russe, francais, coef, desc)


#ouverture du fichier de données et extraction dans listeMots
with open('donnees.txt', 'rb') as fichierBinaire:
    depickler = pickle.Unpickler(fichierBinaire)
    listeMots = depickler.load()


#conversion des coefs en integer

compteur = 0
for a in listeMots:
    a.coef = int(a.coef)
    for i in range(a.coef):
        motConstruct = Mot_jouable(a.russe, a.francais, compteur, a.coef)
        listeTirage.append(motConstruct)
    compteur +=1

for a in listeTirage:
    print(a.coef, a.desc, a.francais, a.russe, a.id)

# jouer:
print("Traduisez en russe le mot qui s'affiche à l'écran, puis appuyez sur la touche ENTREE pour afficher la réponse.")
print("--> Q:quitter\nAprès avoir vu la réponse, entrez X ou V selon si vous aviez trouvé ou non la bonne traduction.\n")


jouer = True
while (jouer):
    
    chance = random.randrange(0, len(listeTirage) -1)
    print("Mot à traduire :", listeTirage[chance].francais)

    choix = input()

    if(choix.find('q') != -1):#quitter
        jouer = False
#affichage de la réponse 
    print("Réponse : ", listeTirage[chance].russe)
#affichage éventuel de la description
    if (listeTirage[chance].desc != ""):
        print("Commentaire : ", listeTirage[chance].desc)

    print("Réussi ?")
    choix = input();
    if(choix.find('x') != -1): #si le joueur a raté
        listeMots[listeTirage[chance].id].coef += 1

    if(choix.find('v') != -1 and listeTirage[chance].coef > 1): #si le joueur a réussi et que le coef est pas déjà égal à 1
        listeMots[listeTirage[chance].id].coef -= 1

    print("État de l'entrée(id = ", listeTirage[chance].id ,") :", listeMots[listeTirage[chance].id].coef,  listeMots[listeTirage[chance].id].desc,  listeMots[listeTirage[chance].id].francais,  listeMots[listeTirage[chance].id].russe)
    print("\n")

    # b = 0
    # for a in listeMots:
    #     print(b, a.coef, a.francais, a.russe)
    #     b+=1
    
# modification du fichier texte une fois la partie terminée.
with open("donnees.txt", "wb") as fichierBinaire:
    pickler = pickle.Pickler(fichierBinaire)
    pickler.dump(listeMots)



fichier.close();

