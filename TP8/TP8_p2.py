import os
import csv
import math as m

import bib

os.chdir(".\\tests")

file1 = "tracesGPS1.csv"
file2 = "tracesGPS2.csv"
file3 = "tracesGPS3.csv"

f = open(file1, "r")
l1 = f.readline()

print("La première ligne : ", l1)



#### solution 1
liste = []
for l in f:
    l = l[:-1]   ## pour éliminer le saut de ligne "\n"
    
    ligne = l.split(",")    ## Créer une ligne à partir des éléments de la ligne

    for i in range(len(ligne)):   ## convertir les valeur en float
        ligne[i] = float(ligne[i])

    liste.append(ligne)   ## ajouter la ligne comme élément ma lilste

#### solution 2   (nécessite le module csv)

f.seek(0)           ## revenir au début du fichier
l1 = f.readline()   ## lire la première ligne

liste2 = []
reader =  csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    ## delimiter="," : pour définir le séparateur
    ## quoting=csv.QUOTE_NONNUMERIC : pour la conversion en float
liste2 = list(reader)

##print(liste2)

print("Premier élément")
print(liste[0])
print("Dernier élément")
print(liste[-1])


print("Nombre de lignes lues : ", len(liste))

# calcul de distance

d = bib.EquiRectDistDeg(liste[0][0], liste[0][1], liste[-1][0], liste[-1][1])
print("La distance est :", d)


