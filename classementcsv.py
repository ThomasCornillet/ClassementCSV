#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""

Ça fonctionne.
À voir si j'ajoute un '.' à l'extension

"""

import os
import csv

# on se déplace dans le dossier cible (évolution possible, lancer le script directement en passant l'adresse du dossier cible en argument
rep = 'n'
while rep == 'n':
	path = input("Quelle est l'adresse du dossier cible ?\n")
	os.chdir(path)
	retval = os.getcwd()
	print("Le dossier courant est {}".format(retval))
	rep = input("Est-ce correct ? o/n\n")

# on crée une liste avec les fichiers du dossier cible
fichiers = os.listdir(path)
nb_fichiers = len(fichiers)

# on crée le csv et son en-tête
fw = open('classement.csv', 'w') # ne pas oublier de fermer avec f.close() lors des tests

entetes = ["nom", "date", "owner", "extension"]
ligneEntete = ",".join(entetes) + "\n"
fw.write(ligneEntete)


i = 1
while i < nb_fichiers:
	valeurs = fichiers[i]
	valeur = valeurs.split(".")
	info = valeur[0]
	extension = valeur[1]
	info = info.split(" - ")
	ligne = ",".join(info) + "," + extension + "\n"
	fw.write(ligne)
	i += 1

fw.close()
