########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe VueBoulet     #
# Proprietaire: JP     #
########################
from Tkinter import *
from tkFont import *
#from Vecteur import *

class VueBoulet:
    def __init__(self, leCanvas = None, leController = None, leVect=None, idTour = None, vitesse = 6):
		#caracteristiques du boulet
        self.leCanvas = leCanvas
        self.leController = leController
        self.leVect = leVect
        self.x = leVect.x1
        self.y = leVect.y1
        self.idTour = idTour
        self.vitesse = vitesse
        self.leBoulet = None
        
        self.affichage()
    
    def affichage(self):
        self.cacher()
		#dessine le boulet sur le canvas
        self.leBoulet = self.leCanvas.create_oval(self.x, self.y, self.x + 7, self.y + 7, fill = "yellow", tags="Boulet")
        
    def cacher(self):
		#efface le boulet du canvas
        self.leCanvas.delete(self.leBoulet)
        
    def deplacement(self):
        self.affichage()
		#detecte si il passe par dessus un autre objet
        objets = self.leCanvas.find_overlapping(self.x-6, self.y-6, self.x+6, self.y+6)
        
        for i in objets:
            lesTags = self.leCanvas.gettags(i)
            if len(lesTags) > 0:
                if lesTags[0] == "Creep": #si un creep est sous le boulet
                    self.cacher()
                    self.leController.getInfoTourVue(self.idTour).detruireBoulet()
                    return
                
        if self.x > 0 and self.y > 0 and self.x < 700 and self.y < 500 and self.x != self.leVect.x2 and self.y != self.leVect.y2:
            self.x = self.x + self.leVect.aUni * self.vitesse ####RECREER UN NOUVEAU VECTEUR SELON LA POSITION DE LA CIBLE A CHAQUE FOIS QUON TIRE
            self.y = self.y + self.leVect.bUni * self.vitesse
            self.leCanvas.after(20, self.deplacement)
        else:
            self.cacher()
            self.leController.getInfoTourVue(self.idTour).detruireBoulet()  