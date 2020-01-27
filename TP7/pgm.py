import cours
import tkinter as tk

def calculer():
    # cette fonction executée à chaque fois qu'on clique sur le bouton "Calculer"
    try :
        d = cours.script(int(l1.get()))
        sv1.set(d["carnets"])
        sv2.set(d["tickets"])
        sv3.set(d["tickets non utilisés"])
        sv4.set(d["total"])
    except:
        print("Erreur de format !!")



Fn = tk.Tk()  # création de la fenêntre graphique
Fn.configure(padx = 30, pady = 30) # configuration des marges de la fenêtre

l1 = tk.Entry(Fn)  # champs de saisie de texte
b1 = tk.Button(Fn, text="Calculer", command=calculer)  # bouton Calculer

# placement de l1 et b1 sur la fenêtre  
b1.grid(column=1, row = 0)
l1.grid(column=0, row=0)

# création des labels
la1 = tk.Label(Fn, text="Carnets : ")
la2 = tk.Label(Fn, text="Tickets : ")
la3 = tk.Label(Fn, text="Non utilisés : ")
la4 = tk.Label(Fn, text="Total : ")

# Placement des labels
la1.grid(column=0, row = 1, sticky = "W")
la2.grid(column=0, row = 2, sticky = "W")
la3.grid(column=0, row = 3, sticky = "W")
la4.grid(column=0, row = 4, sticky = "W")


# Création des labels à veleurs variables
sv1 = tk.StringVar()
lv1 = tk.Label(Fn, textvariable = sv1)
sv2 = tk.StringVar()
lv2 = tk.Label(Fn, textvariable = sv2)
sv3 = tk.StringVar()
lv3 = tk.Label(Fn, textvariable = sv3)
sv4 = tk.StringVar()
lv4 = tk.Label(Fn, textvariable = sv4)

# Placement des labels à veleurs variables
lv1.grid(column=1, row = 1)
lv2.grid(column=1, row = 2)
lv3.grid(column=1, row = 3)
lv4.grid(column=1, row = 4)

Fn.mainloop()

