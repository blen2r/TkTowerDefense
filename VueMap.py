########################
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
# Yann David           #
#                      #
#                      #
# Classe Map           #
# Proprietaire: Yann   #
########################

from Tkinter import *
from tkFont import *
from Map import *
from Constantes import *

class VueMap:
    
    def __init__(self, leCanvas = None,leController=None, colorFill="blue"):
        self.leCanvas = leCanvas
        self.leController=leController
        self.laMap = leController.getMap()
        #self.intI = 0
        #self.intJ = 0
        self.colorFill = colorFill
        self.dessin = None
    
    def dessinerMap(self):
		#dessine la map selon les chiffres presents dans le fichier texte associe a chaque map
        compteY = 0
        for i in self.laMap.matrice:
            compteX = 0
            for j in i:
                if j == '1' or j == '2':
                    self.dessin = self.leCanvas.create_rectangle( compteX*Constantes.DIMX, compteY*Constantes.DIMY, compteX*Constantes.DIMX+Constantes.DIMX, compteY*Constantes.DIMY+Constantes.DIMY, fill=self.colorFill, width=0)
                compteX = compteX + 1 
            compteY = compteY + 1
    
    def placerVecteurs(self):
        pass
