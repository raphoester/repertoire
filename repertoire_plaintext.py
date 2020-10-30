import random
import os
print(os.getcwd())
os.chdir("C:\\Users\\admin\\Desktop\\repertoire_2.0")
fichier = open("repertoire.txt", encoding='utf-8' , mode="r")
# fichier.close();
listeMots = []
motCourant = ""

class Mot: 
    def __init__ (soi, russe, francais, coef=1, desc=""):
        soi.russe = russe
        soi.francais = francais
        soi.coef = coef
        soi.desc = desc



ligne = "init"
compteur = 0;

while (ligne != ""):
    compteur +=1
    ligne = fichier.readline()
    if (ligne == ""):
        break;
    ligne = ligne.split('|')

    if (len(ligne) == 4 ): #s'il y a un commentaire
        motCourant = Mot(ligne[0], ligne[1], ligne[2], ligne[3])
    elif (len(ligne) == 3): #s'il n'y a pas de commentaire.
        motCourant = Mot(ligne[0], ligne[1], ligne[2])
    else:
        print("fichier texte corrompu pour l'entrée suivante : ", compteur)
    
    listeMots.append(motCourant)

for a in listeMots:
    a.coef = int(a.coef)


# jouer:
print("Traduisez en russe le mot qui s'affiche à l'écran, puis appuyez sur la touche ENTREE pour afficher la réponse.")
print("--> Q:quitter\nAprès avoir vu la réponse, entrez X ou V selon si vous aviez trouvé ou non la bonne traduction.\n")

jouer = True
while (jouer):
    
    chance = random.randrange(0, len(listeMots) -1)
    print("Mot à traduire :", listeMots[chance].francais)

    choix = input()

    if(choix.find('q') != -1):#quitter
        jouer = False

    print("Réponse : ", listeMots[chance].russe )
    if (listeMots[chance].desc != ""):
        print("Commentaire : ", listeMots[chance].desc)
    print("Réussi ?")
    choix = input();
    if(choix.find('x') != -1): #si le joueur a raté
        listeMots[chance].coef += 1

    if(choix.find('v')!= -1 and listeMots[chance].coef > 1):#si le joueur a réussi
        listeMots[chance].coef -= 1

    print("État de l'entrée :", listeMots[chance].coef, listeMots[chance].desc, listeMots[chance].francais, listeMots[chance].russe)
    print("\n")
    
# modification des coefficients du fichier texte.

fichier.close();

