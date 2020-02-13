import tkinter as tk
from tkinter import ttk
import os
import csv
import bib

def calculer():
    try:
        f = open(".\\tests\\" + files.get(), "r")
        fl = f.readline()
        liste = []
        reader =  csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        liste = list(reader)

        sv2.set(str(len(liste)))
        sv3.set(str(liste[0][0])+ "," + str(liste[0][1]))
        sv4.set(str(liste[-1][0])+ "," + str(liste[-1][1]))

        d = bib.EquiRectDistDeg(liste[0][0], liste[0][1], liste[-1][0], liste[-1][1])
        sv1.set(str(d))

        
        
    except:
        print("Erreur !!")
  

fen = tk.Tk()
fen.title("Traces GPS")

fen.geometry("377x191") #You want the size of the app to be 500x500
fen.resizable(0, 0) #Don't allow resizing in the x or y direction

tk.Grid.rowconfigure(fen, 0, weight=1)
tk.Grid.columnconfigure(fen, 0, weight=1)


l = os.listdir(".\\tests")
ll = [e for e in l if ".csv" in e]
files = ttk.Combobox(fen, values=ll)

fen.configure(padx = 30, pady = 30)

files.grid(column = 0, row = 0, columnspan = 2, sticky = "WENS")

l1 = tk.Label(text = "Distance :")
l2 = tk.Label(text = "Nombre de ligne:")
l3 = tk.Label(text = "1ere ligne :")
l4 = tk.Label(text = "dernière ligne :")

l1.grid(column = 0, row = 1, sticky = "W")
l2.grid(column = 0, row = 2, sticky = "W")
l3.grid(column = 0, row = 3, sticky = "W")
l4.grid(column = 0, row = 4, sticky = "W")

b = tk.Button(text="Calculer", command=calculer)
b.grid(column = 0, row = 5, columnspan = 2)

sv1 = tk.StringVar()
lv1 = tk.Label(textvariable = sv1)
sv2 = tk.StringVar()
lv2 = tk.Label(textvariable = sv2)
sv3 = tk.StringVar()
lv3 = tk.Label(textvariable = sv3)
sv4 = tk.StringVar()
lv4 = tk.Label(textvariable = sv4)

lv1.grid(column = 1, row = 1, sticky = "E")
lv2.grid(column = 1, row = 2, sticky = "E")
lv3.grid(column = 1, row = 3, sticky = "E")
lv4.grid(column = 1, row = 4, sticky = "E")

fen.mainloop()

