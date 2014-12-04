########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe VueRange      #
# Proprietaire: JP     #
########################

class VueRange:
    def __init__(self, leCanvas = None, leController = None, idTour = None):
        self.leCanvas = leCanvas
        self.leControlleur = leController
        self.idTour = idTour
        self.lesElements = []
        self.leRange = None
        self.rangeInvisible = None
        self.rangeTour = None
        self.level = 2
        
    def affichage(self):
		#affiche le range de la tour selon la position de celle-ci ainsi que son lvl
        self.leCanvas.delete(self.leRange)
        self.leCanvas.delete(self.rangeInvisible)
        self.rangeTour = self.leControlleur.getInfoTour(self.idTour).range
        self.posX = self.leControlleur.getInfoTour(self.idTour).x
        self.posY = self.leControlleur.getInfoTour(self.idTour).y
        self.level = self.leControlleur.getInfoTour(self.idTour).lvl+1
        self.leRange = self.leCanvas.create_oval(self.posX - self.rangeTour*self.level, self.posY - self.rangeTour*self.level, self.posX + self.rangeTour*self.level, self.posY + self.rangeTour*self.level, outline="red", width=2)#, fill = "gray")
        
        
    def detection(self):
        self.leCanvas.delete(self.rangeInvisible)
        self.rangeTour = self.leControlleur.getInfoTour(self.idTour).range #ici car on peut changer le range en upgradant
        self.posX = self.leControlleur.getInfoTour(self.idTour).x
        self.posY = self.leControlleur.getInfoTour(self.idTour).y
        self.rangeInvisible = self.leCanvas.create_oval(self.posX - self.rangeTour*self.level, self.posY - self.rangeTour*self.level, self.posX + self.rangeTour*self.level, self.posY + self.rangeTour*self.level)
        
        lesElements = self.leCanvas.find_overlapping(self.posX - self.rangeTour*self.level, self.posY - self.rangeTour*self.level, self.posX + self.rangeTour*self.level, self.posY + self.rangeTour*self.level)
        
        
        if self.leControlleur.getInfoTour(self.idTour).cible == None: #si pas de cible, on cherche une cible
            for i in lesElements:
                lesTags = self.leCanvas.gettags(i)
                if len(lesTags) > 0:
                    if lesTags[0] == "Creep": #si un creep est dans le range
                            self.leControlleur.getInfoTour(self.idTour).cible = self.leControlleur.getInfoCreep(int(lesTags[1])) #on lui donne cette cible la
        elif self.leControlleur.getInfoCreep(self.leControlleur.getInfoTour(self.idTour).cible.idCreep) == None: #si le creep est mort
            self.leControlleur.getInfoTourVue(self.idTour).detruireBoulet()
            self.leControlleur.getInfoTour(self.idTour).cible = None
        else: #si on a une cible
            #print self.leControlleur.getInfoTour(self.idTour).cible.idCreep
            dansZone = False
            
            for i in lesElements:
                lesTags = self.leCanvas.gettags(i)
                if len(lesTags) > 0:
                    if lesTags[0] == "Creep" and lesTags[1] == str(self.leControlleur.getInfoTour(self.idTour).cible.idCreep): #si le creep cible est dans le range
                        dansZone = True
                        
            if dansZone == True:
                #print "attaque"+str(self.leControlleur.getInfoTour(self.idTour).cible.idCreep)
                self.leControlleur.interface.root.after(100/self.leControlleur.getInfoTour(self.idTour).vitesse, self.leControlleur.getInfoTour(self.idTour).attaquer)
            else:
                self.leControlleur.getInfoTourVue(self.idTour).detruireBoulet()
                self.leControlleur.getInfoTour(self.idTour).cible = None
                
                
        self.leCanvas.delete(self.rangeInvisible)
        
    def cacher(self):
		#efface le range du canvas
        self.leCanvas.delete(self.leRange)
