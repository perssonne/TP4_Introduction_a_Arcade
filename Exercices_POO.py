#Question 1

class StringFoo:
    def __init__(self):
        self.attribut = None

    def set_string(self, parametre):
        self.attribut = parametre

    def print_string(self):
        print(self.attribut.upper())

stringfoo = StringFoo()
stringfoo.set_string('Hello World!')
stringfoo.print_string()

#Question 2

class Rectangle:
    def __init__(self, largeur, longueur):
        self.longueur = longueur
        self.largeur = largeur

    def calcul_aire(self):
        return self.largeur*self.longueur

    def afficher_infos(self):
        print('Longueur:', self.longueur)
        print('Largeur:', self.largeur)
        print('Aire:', self.calcul_aire())

rectangle = Rectangle(3,6)
rectangle.afficher_infos()

#Question 3

from math import pi

class Cercle:
    def __init__(self, rayon, diametre):
        self.rayon = rayon
        self.diametre = diametre
        self.pi = pi

    def calcul_aire(self):
        return self.pi*(self.rayon*self.rayon)

    def calcul_circonference(self):
        return self.pi*self.diametre

    def afficher_infos(self):
        print('Rayon:', self.rayon)
        print('Diametre:', self.diametre)
        print('Circonference:', self.calcul_circonference())
        print('Aire:', self.calcul_aire())

cercle = Cercle(3,4)
cercle.afficher_infos()






