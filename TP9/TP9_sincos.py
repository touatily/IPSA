import numpy as np
import matplotlib.pyplot as pp

xstt = -np.pi  # min x
xend = np.pi   # borne supp x
ystt = -1      # min x
yend = 1       # max y
step = 0.1     # le pas

lx = np.arange(xstt, xend, step)  # la valeur de xend n'appartient pas à lx

#ly = np.sin(lx)              # solution 1 : sin de numpy
#ly = list(map(np.sin, lx))   # solution 2 : map
ly = [np.sin(x) for x in lx]  # solution 3 : comprehension de liste

ly2 = [np.cos(x) for x in lx]

pp.plot(lx, ly, label="Courbe sinus")      # courbe sin
pp.plot(lx, ly2, label="Courbe Cosinus")   # courbe cos
pp.legend()                                # afficher la légende (les labels) 
pp.grid()                                  # affichier la grille

pp.axis([xstt, xend, ystt, yend])       # définition des bornes du rendu (petit espace du coté droit)
#pp.axis([xstt, max(lx), ystt, yend])   # définition des bornes du rendu (pas d'espace)


pp.savefig(fname="courbe1PB2.svg", format="svg") # fichier texte / vectorielle
pp.savefig(fname="courbe1PB2.eps", format="eps") # fichier texte / vectorielle
pp.savefig(fname="courbe1PB2.png", format="png") # fichier binaire / carte de points
pp.savefig(fname="courbe1PB2.pdf", format="pdf") # fichier binaire / vectorielle

pp.show()           # afficher la fenetre des courbes.



