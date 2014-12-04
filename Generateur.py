########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Generateur    #
# Proprietaire: PE     #
########################

from Tkinter import *
from Creep import *

class Generateur:
    def __init__(self, x=0, y=0, tempsVagues=10000, tempsCreep=1000, leController=None, actif=True, partieEnCours=False, nbrCreepsParVague=5):
        self.x = x
        self.y = y
        self.tempsVagues = tempsVagues
        self.tempsCreep = tempsCreep
        self.leController = leController
        self.actif=actif
        self.partieEnCours = partieEnCours
        self.creepsCrees = 0
        self.nbrCreepsParVague = nbrCreepsParVague
        self.nbrVagues = 1
        self.jouer = True
        
        self.generer()
        
    def change(self): #sert a changer le status du generateur
        if self.actif == True:
            self.actif = False
        else:
            self.actif = True
            self.generer()
    
    def generer(self):
        if self.jouer == True: #si joueur vivant
            if self.partieEnCours == True: #si partie en cours
                if self.actif == True:
                    self.leController.creerCreep()
                    #print "Creep cree" #debug
                    self.leController.interface.root.after(self.tempsCreep, self.generer) #un creep a chaque x milisecondes
                    self.creepsCrees = self.creepsCrees+1
                    if self.creepsCrees == self.nbrCreepsParVague: #si on a fait assez de creeps pour la vague, on pause jusqu'a la prochaine vague
                        self.change()
                else: #on reset pour la prochaine vague
                   # print "En pause" #debug
                    self.creepsCrees = 0
                    self.nbrVagues = self.nbrVagues + 1
                    self.leController.interface.root.after(self.tempsVagues, self.change)