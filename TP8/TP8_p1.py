import os

#### Question 1

# solution 1
p1 = os.getcwd()
print("Le répertoire courant est :", p1)

# solution 2
p2 = os.path.realpath(".")
print("Le répertoire courant est :", p2)


d = os.path.dirname(p1)  # récupérer le nom du répertoire qui le contient
b = os.path.basename(p1) # récupérer juste le nom du répertoire courant

print("Le répertoire :", d)
print("Le nom du répertoire", b)

#### Question 2

print("Contenu du répertoire courant : ")
l = os.listdir(".")
for e in l:
    print("\t", e)

#### Question 3

os.chdir(".\\tests")      ## chemin relatif
os.chdir(p1 + "\\tests")  ## chemin absolu

p1 = os.getcwd()
print("Le nouveau répertoire courant est :", p1)

#### Question 4

print("Le contenu du répertoire ./tests : ")
l = os.listdir(".")
for  e in l:
    print("\t", e)

##### Exo 2
#### Question 1
file = "MontyPython_TheGalaxySong.txt"

# solution 1
f = open(file, "r")   # ouverture du fichier
c1 = f.read()         # lecture de tout le fichier
print(c1)
f.close()

# solution 2
f = open(file, "r")
l = f.readlines()     # récupérer le contenu du fichier dans une liste 
for e in l:
    print(e, end="")

# solution 3
f.seek(0)             # remettre le curseur au premier caractère du fichier
for l in f:
    print(l, end="")
    
# solution 4
f.seek(0)
while True:
    l = f.readline()
    if not l:
        break
    else:
        print(l, end="")
f.close()

##### Exo 3
#### Question 1 & 2 & 3

def cherche_lignes(file, mot):
    f = open(file, "r")
    ls = f.readlines()
    r = [e for e in ls if mot in e] # comprehension de liste
    return r

resultat = cherche_lignes("MontyPython_TheGalaxySong.txt", "miles")

for e in resultat:
    print(e, end="")

print("le nombre de lignes contenant 'miles' :", len(resultat))

outfile = "out.txt"
fout = open(outfile, "w")           # ouverture en mode ecriture
fout.write("MontyPython_TheGalaxySong.txt" + "\n" + str(len(resultat)))
fout.close()                        # très très important !!!! Si on ne ferme pas le fichier, l'écriture ne se fait de suite 


