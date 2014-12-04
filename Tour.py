########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Tour          #
# Proprietaire: JP     #
########################

class TourBase:
    def __init__(self, x = 0, y = 0, range = 70, lvl = 1, idTour = None, force=40, vitesse=1, nbrTirs=1, leController=None):
        self.x = x
        self.y = y
        self.range = range
        self.idTour = idTour
        self.vitesse = vitesse
        self.force = force
        self.nbrTirs = nbrTirs
        self.visibilite = False
        self.lvl = lvl
        self.cible = None
        self.leController = leController
        
    def tirer(self):
        self.projectile = Boulet(self.x, self.y)
        degat = force * lvl
                
    def monterNiveau(self, lvl):
        self.lvl = lvl + 1
        
    def attaquer(self):
        #print "attaque"
        self.cible.gererVie(self.force*self.lvl)
        self.leController.getInfoTourVue(self.idTour).creerBoulet(self.cible)
        
class TourStandard(TourBase):
    cout = 50
    def __init__(self, x = 0, y = 0, range = 35, lvl = 1, idTour = None, force=6, leController=None):
        TourBase.__init__(self, x = x, y = y, range = range, lvl = lvl, idTour = idTour, force=force, leController=leController)

    
        
        
        
        