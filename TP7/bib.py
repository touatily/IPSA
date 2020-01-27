import math as m
import turtle

def reduction(age):
    """
    Fonction qui calcule la réduction selon l'age
    """
    if age < 10:
        r = 50
    elif age <= 18:
        r = 30
    elif age >= 60 :
        r = 20
    else:
        r = 0
    return r

def script(n):
    """
    Fonction qui retourne un dictionnaire contenant les informations
        nombre de carnets, nombre de tickets à acheter, nombre de tickets non utilisés
        et le prix total.
        La fonction prend en paramètre le nombre de voyages.
    """
    c = n//10
    if n%10 >= 8:
        c += 1
        notused = c * 10 - n
        t = 0
        p = c * 14.90
    else:
        notused = 0
        t = n%10
        p = c * 14.90 + t * 1.90

    return {"carnets" : c, "notused" : notused
            , "tickets" : t, "prix" : p}

def drawvonKoch(taille):
    """
        Fonction qui dessine la courbe fractale de Von Koch
    """
    if taille <= 5:
        turtle.forward(taille)
    else:
        drawvonKoch(taille/3)
        turtle.left(60)
        drawvonKoch(taille/3)
        turtle.right(120)
        drawvonKoch(taille/3)
        turtle.left(60)
        drawvonKoch(taille/3)

# partie programme principale.
if __name__ == "__main__":

    # Exo 3
    turtle.speed("fastest") # fixer la vitesse de la tortue ^^
    drawvonKoch(100)

    """
    # Exo 2

    while True:
        q = input("Saisir nombre de voyage (autre chose pour quitter) : ")
        try:
            q = int(q)
            print(script(q))
        except ValueError:
            print("Erreur :  Au revoir")
            break
    """

