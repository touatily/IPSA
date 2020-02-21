import matplotlib.pyplot as pp
import csv
import matplotlib.image as pm


# Il faut mettre les fichiers dans le même répertoire que le programme
file1 = "tracesGPS1.csv"
file2 = "tracesGPS2.csv"
file3 = "tracesGPS3.csv"

# Ouverture des fichiers en mode lecture
f1 = open(file1, "r")
f2 = open(file2, "r")
f3 = open(file3, "r")

# Ignorer la première ligne "entête".
f1.readline()
f2.readline()
f3.readline()

# On utilise le module csv pour lire les données des fichiers.
# delimiter="," : pour préciser que le séparateur est la virgule.
# quoting = csv.QUOTE_NONNUMERIC : pour convertir les données en flottants
r1 = csv.reader(f1, delimiter=",", quoting = csv.QUOTE_NONNUMERIC)
l1 = list(r1)
r2 = csv.reader(f2, delimiter=",", quoting = csv.QUOTE_NONNUMERIC)
l2 = list(r2)
r3 = csv.reader(f3, delimiter=",", quoting = csv.QUOTE_NONNUMERIC)
l3 = list(r3)


# Fermeture des fichiers.
f1.close()
f2.close()
f3.close()

# Lecture de l'image. L'image doit se trouver dans le même répertoire.
img = pm.imread('SatIvry.png')
# Ajouter l'image comme arrière plan à notre fenêtre figure.
pp.imshow(img, extent = [2.382,2.394, 48.811,48.815])



lx1 = [l[1] for l in l1] # récupérer la longitude (deuxième colonne)
ly1 = [l[0] for l in l1] # récupérer la latitude  (première colonne)
pp.plot(lx1, ly1, color='green', marker='*')   # dessin du premier trajet

lx2 = [l[1] for l in l2]
ly2 = [l[0] for l in l2]
pp.plot(lx2, ly2, color='red', marker='o')     # dessin du premier trajet

lx3 = [l[1] for l in l3]
ly3 = [l[0] for l in l3]
pp.plot(lx3, ly3, color='blue', marker='.')    # dessin du premier trajet

pp.show()

