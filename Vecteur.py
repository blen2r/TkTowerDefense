########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Vecteur       #
# Proprietaire: PE     #
########################

from math import sqrt

class Vecteur:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        #Point d'origine et d'arrivee
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        #Composants
        self.a = self.x2 - self.x1
        self.b = self.y2 - self.y1
        
        #Norme
        self.norme = sqrt( self.a*self.a + self.b*self.b ) 
        
        #Composants du vecteur unitaire
        self.aUni = self.a/self.norme
        self.bUni = self.b/self.norme