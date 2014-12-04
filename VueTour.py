########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe VueTour       #
# Proprietaire: JP     #
########################
from Tkinter import *
from tkFont import *
from VueBoulet import *
from Vecteur import *

class VueTour:
    def __init__(self, leCanvas = None, leController = None, idTour = -1, leRange=None):
        self.leCanvas = leCanvas
        self.leControlleur = leController
        self.idTour = idTour
        self.laTour = None
        self.leRange = leRange
        self.leBoulet = None
         
    def affichage(self, valide):
		#affiche la tour selon le modele de tour choisi si le placement est valide, sinon un carre rouge s'affiche. Apres le clique, place la tour si l'emplacement est valide
        self.valide = valide
        posX = self.leControlleur.getInfoTour(self.idTour).x
        posY = self.leControlleur.getInfoTour(self.idTour).y
        if valide == True:
            self.imTour = PhotoImage(file=self.leControlleur.interface.skin+"butTour.gif")
        else:
            self.imTour = PhotoImage(file=self.leControlleur.interface.skin+"invalide.gif")
        self.leCanvas.delete(self.laTour)
        self.laTour = self.leCanvas.create_image(posX-25, posY-25, anchor=NW, image = self.imTour, tags=("Tour", str(self.idTour)))
            
    def cacher(self):
		#efface la tour du canvas
        self.leCanvas.delete(self.laTour)
        
    def detruireBoulet(self):
		#efface le boulet tirer par la tour
        if self.leBoulet != None:
            self.leBoulet.cacher()
        self.leBoulet = None
        
    def creerBoulet(self, cible=None):
		#creer un objet boulet a chaque tir de la tour
        if self.leBoulet == None:
            vect = Vecteur(x1=self.leControlleur.getInfoTour(self.idTour).x, y1=self.leControlleur.getInfoTour(self.idTour).y, x2=self.leControlleur.getInfoTour(self.idTour).cible.x, y2=self.leControlleur.getInfoTour(self.idTour).cible.y)
            self.leBoulet = VueBoulet(leCanvas=self.leCanvas, leController= self.leControlleur, idTour=self.idTour, leVect=vect)
        else:
            self.leBoulet.deplacement()
        
        
        