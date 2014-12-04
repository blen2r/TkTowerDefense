########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe VueJeu        #
# Proprietaire: PE     #
########################

#imports
from Tkinter import *
from tkFont import *
from Popup import *
from VueMap import *

#from Controller import *

################
#from Creep import *
from VueCreep import *
################

class VueJeu:
    def __init__(self, leController=None, zoneJeu=None, laVue=None):
        self.leController = leController
        self.zoneJeu = zoneJeu
        self.laVue = laVue
        
        self.imageJeu = PhotoImage(file=self.laVue.skin+"zoneJeu.gif") #image de la map
        self.fondJeu = self.zoneJeu.create_image(0, 0, anchor=NW, image=self.imageJeu) #fond du jeu
        
        self.laVueMap = VueMap(leCanvas=self.zoneJeu, leController=self.leController)
        self.laVueMap.dessinerMap()
        
        
        #evenements
        self.zoneJeu.bind("<Motion>", self.mouseMove)   
        self.zoneJeu.bind("<Button-1>", self.mouseClick)
        
        
        #trucs a faire pour le jeu, a penser: comment deplacer ca pour que la job soit faite par le controller
        
    #si position valide, on place la tour, aPlacer=None,
    def mouseClick(self, event):
        if self.leController.aPlacer != None:
            self.leController.appliquerTour()
        else:
            self.leController.selectionTour(event)
    
    def mouseMove(self,event):
        if self.leController.aPlacer != None:
            self.leController.deplacerObjets(event)
