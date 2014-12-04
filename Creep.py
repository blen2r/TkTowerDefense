########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Creep         #
# Proprietaire: JP     #
########################

from Constantes import *

class Creep:
    def __init__(self, x = 0, y = 0, vitesse = 4, force = 10, pv = 200, visibilite = True, idCreep = None, leNumVecteur=0, leController=None):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.force = force
        self.pv = pv #vie
        self.visibilite = visibilite #pas utilise dans cette version, sert pour les creeps invisibles
        self.idCreep = idCreep
        self.leController = leController
        self.leNumVecteur = leNumVecteur
        self.leVecteur = leController.getMap().vectListe[leNumVecteur] #vecteur de deplacement
    
        
    def deplacement(self):
        condition = None
        if self.leVecteur.a < 0 or self.leVecteur.b < 0: #dependamment de l'orientation du vecteur, on regarde dans ce sens si sorti du chemin
            condition = self.x <= self.leVecteur.x2*Constantes.DIMX and self.y <= self.leVecteur.y2*Constantes.DIMY
        else:
            condition = self.x >= self.leVecteur.x2*Constantes.DIMX and self.y >= self.leVecteur.y2*Constantes.DIMY
            
        if condition: #si sorti du chemin
            self.leNumVecteur = self.leNumVecteur + 1 #change de vecteur
            if self.leNumVecteur < len(self.leController.getMap().vectListe): #si pas arrive au chateau, on continue
                self.leVecteur = self.leController.getMap().vectListe[self.leNumVecteur]
                self.x = self.leVecteur.x1*Constantes.DIMX
                self.y = self.leVecteur.y1*Constantes.DIMY
            else: #si au chateau, on enleve des points de vie au joueur et detruit le creep
                self.leController.leJoueur.enleverPtsVie(self.force)
                self.leController.interface.actualiserVieArgent()
                self.leController.detruireCreep(self.idCreep)
        else: #sinon on avance
            self.x = self.x + self.leVecteur.aUni * self.vitesse
            self.y = self.y + self.leVecteur.bUni * self.vitesse
        
    def gererVie(self, forceTour = 0):
        self.pv = self.pv - forceTour
        if self.pv <= 0:
            self.leController.detruireCreep(self.idCreep, False)
        