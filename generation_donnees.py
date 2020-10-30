#script servant à générer le fichier donnees.txt nécessaire à l'exécution du répertoire pédagogique - à partir du fichier repertoire.txt au format texte brut. 

import random
import os
import pickle


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



with open("donnees.txt", "wb") as fichierBinaire:
    pickler = pickle.Pickler(fichierBinaire)
    pickler.dump(listeMots)
