########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe VueCreep      #
# Proprietaire: JP     #
########################
from Tkinter import *
from tkFont import *
from Constantes import *

class VueCreep:
    def __init__(self, leCanvas = None, leController = None, idCreep = None):
		#caracteristiques du creep
        self.leCanvas = leCanvas
        self.leControlleur = leController
        self.idCreep = idCreep
        self.leCreep = None
        
    def affichage(self): 
		#affiche le creep a la bonne position
        self.leCanvas.delete(self.leCreep)
        posX = self.leControlleur.getInfoCreep(self.idCreep).x
        posY = self.leControlleur.getInfoCreep(self.idCreep).y
        self.leCreep = self.leCanvas.create_oval(posX, posY, posX + Constantes.DIMX, posY + Constantes.DIMY, fill = "red", tags=("Creep", str(self.idCreep)))
        
    def cacher(self):
		#delete le creep
        self.leCanvas.delete(self.leCreep)