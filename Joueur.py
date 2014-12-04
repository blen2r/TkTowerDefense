########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Joueur        #
# Proprietaire: Yann   #
########################

class Joueur:
    def __init__(self, ptsDeVie=100, argent=120):
        self.ptsDeVie = ptsDeVie
        self.argent = argent
        self.vivant = True
        self.nom = None
        
    def enleverPtsVie(self,nbPtsEnleve=1):
        self.ptsDeVie = self.ptsDeVie - nbPtsEnleve
        if self.ptsDeVie <= 0:
            self.vivant = False
    
    def enleverArgent(self,nbArgentEnleve=1):
        self.argent = self.argent - nbArgentEnleve
         
    def ajouterArgent(self,nbArgentAjoute=1):
        self.argent = self.argent + nbArgentAjoute