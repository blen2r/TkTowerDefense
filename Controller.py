########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Controller    #
# Proprietaire: PE     #
########################

from Vue import *
from Creep import *
from Tour import *
from VueTour import *
from VueRange import *
from Joueur import *
from Map import *
from Generateur import *
from Score import * 

class Controller:
    def __init__(self):
        #variables
        self.nbrParties = 0 #nombre de parties jouees
        self.aPlacer = None #objet a placer sur la map
        self.aPlacerVue = None #objet visuel a placer
        self.tourSelect = None
        self.leJoueur = Joueur() 
        
        self.lesTours = [] #liste des tours existantes
        self.lesToursVue = [] #liste des representations graphiques des tours
        self.lesCreeps = [] #liste des creeps existants
        self.lesCreepsVue = [] #liste des affichages de creeps existants
        
        #les ids
        self.idCreep = 0 #id a donner a chaque creep, incremente
        self.idTour = 0 #meme chose pour les tours
        self.nbrCreepsTues = 0
        
        #map
        self.nomMap = "" #fichier contenant la map
        self.laMap = None #objet Map
        self.generateurCreep = None #entite qui controle d'ou les creeps arrivent et a quel rythme
        
        #interface
        self.interface = Vue(leController=self)
        
        #scores
        self.lesScores = Score(leController=self)
        
        #actions a faire en ouvrant le jeu
        self.interface.chargerMenu()
        self.interface.root.mainloop() #derniere fonction du constructeur
        
    def chargerMap(self): #init la map
        self.laMap = Map(nomMap="Maps/"+self.nomMap)
        xGen, yGen = self.laMap.getPosGenerateur()
        self.generateurCreep = Generateur(x=xGen, y=yGen, leController=self)
        
    def jeuDebut(self): #actions a faire en debut de jeu
        self.leJoueur = Joueur()
        self.leJoueur.vivant = True
        self.nbrCreepsTues = 0
        self.interface.actualiserVieArgent()
        
    def reset(self): #a chaque fois qu'on clique sur "nouvelle partie"
        #variables
        self.aPlacer = None #objet a placer sur la map
        self.aPlacerVue = None #objet visuel a placer
        self.tourSelect = None
        
        self.lesTours = [] #liste des tours existantes
        self.lesToursVue = [] #liste des representations graphiques des tours
        self.lesCreeps = [] #liste des creeps existants
        self.lesCreepsVue = [] #liste des affichages de creeps existants
        
        #les ids
        self.idCreep = 0 #id a donner a chaque creep, incremente
        self.idTour = 0 #meme chose pour les tours
        self.nbrCreepsTues = 0
        
        #map
        self.nomMap = ""
        self.laMap = None
        self.generateurCreep = None
        
        self.jeuDebut()
        
    def getMap(self): #retourne l'objet Map pour avoir acces a ses donnees
        return self.laMap
    
    def getInfoJoueur(self): #retourne l'objet Joueur pour avoir acces a ses donnees
        return self.leJoueur
    
    def getInfoTour(self, id): #retourne la tour associee a cet id
        for i in self.lesTours:
            if i.idTour == id:
                return i
            
    def getInfoTourVue(self, id): #retourne la vue de la tour associee a cet id
        for i in self.lesToursVue:
            if i.idTour == id:
                return i
    
    def getInfoRange(self, id): #retourne la tour associee a cet id
        for i in self.lesRangesVue:
            if i.idTour == id:
                return i
        
    
    def getInfoCreep(self, id): #retourne le creep associe a cet id
        for i in self.lesCreeps:
            if i.idCreep == id:
                return i 
            
            
    def getInfoCreepVue(self, id): #retourne le creep associe a cet id
        for i in self.lesCreepsVue:
            if i.idCreep == id:#
                #print i.idCreep
                return i
            
    def boucleJeu(self):
        if self.leJoueur.vivant == True:
            for i in self.lesCreeps:
                #print i.idCreep #debug
                self.getInfoCreepVue(i.idCreep).affichage()
                i.deplacement() 
            
            for i in self.lesToursVue:
                i.leRange.detection() #on cherche des cibles
                
            self.interface.root.after(200, self.boucleJeu) #"boucle"
        else: #si le joueur est mort
            self.generateurCreep.jouer=False #arretter de generer des creeps pour une periode indefinie
            self.interface.dechargerJeu()
            self.leJoueur.points = self.nbrCreepsTues*2 + self.leJoueur.argent #on calcule le score
            self.interface.unPopup = PopupEntreNom(leController=self) #on veut enregistrer le score
                
        
    def creerCreep(self): #ajouter un nouveau creep a la liste des creeps, lui associer une vue et un id 
        self.lesCreeps.append(Creep(x=self.generateurCreep.x, y=self.generateurCreep.y, idCreep=self.idCreep, leController=self, pv=100+100*self.generateurCreep.nbrVagues/2))
        self.lesCreepsVue.append(VueCreep(leCanvas=self.interface.zoneJeu, leController=self, idCreep=self.idCreep))
        
        self.idCreep = self.idCreep + 1  #incremente l'id du prochain creep
        
    
    
    def detruireCreep(self, id, auChateau=True):
        if auChateau == False: #un creep a ete tue, on donne des points
            self.nbrCreepsTues = self.nbrCreepsTues +1
            self.leJoueur.argent = self.leJoueur.argent + 10
            self.interface.actualiserVieArgent()
            
        for i in self.lesCreeps: #enlever le creep de la liste
            if i.idCreep == id:
                self.lesCreeps.remove(i)
                #print "creep removed"
                
        for j in self.lesCreepsVue: #enlever la vue associee a ce creep
            if j.idCreep == id:
                j.cacher()
                self.lesCreepsVue.remove(j)
                #print "creepVue removed"
                
    
    def choisirLevelTour(self, type): #on a clique sur un bouton de tour
        if self.aPlacer == None: #aucune tour selectionnee, on choisis ce qu'on veut
            self.interface.unPopup = PopupChoixTour(leCanvas=self.interface.zoneJeu, x=350, y=100, leController=self, typeTour=type) #popup pour choisir le level de la tour et le prix
        else:
            self.annulerTour() #on a deja selectionne une tour, on la deselectionne
    
    def creerTour(self, type=None, level=1):
        #creer un objet tour, tourVue..., les associer, retourner l'objet vue a afficher
        self.aPlacer = type(lvl=level, idTour=self.idTour, leController=self)
        rangeTemp = VueRange(leCanvas=self.interface.zoneJeu, leController=self, idTour=self.idTour)
        self.aPlacerVue = VueTour(leCanvas=self.interface.zoneJeu, leController=self, idTour=self.idTour, leRange=rangeTemp)
        
        #ajouter aux listes
        self.lesTours.append(self.aPlacer)
        self.lesToursVue.append(self.aPlacerVue)
        
        self.idTour = self.idTour + 1
    
    def listeTypesTours(self): #retourne tous les types de tours existants pour avoir assez de boutons et les associer aux bonnes cmd
        return (TourStandard,)
    
    def appliquerTour(self):#, skip=False):
        if self.empVal == True:
            self.laMap.changerEmplacement(self.aPlacer.x, self.aPlacer.y)
            self.aPlacerVue.leRange.cacher() #on cache le range car on construit la tour
            self.leJoueur.enleverArgent(self.aPlacer.cout*self.aPlacer.lvl)#enlever de l'argent au joueur
            self.interface.actualiserVieArgent()
            self.aPlacer = None #on efface les objets temporaires
            self.aPlacerVue = None
            self.interface.zoneJeu.config(cursor="") #on reset le curseur
        
    def annulerTour(self):
        #on cache la tour et son range
        self.aPlacerVue.cacher()
        self.aPlacerVue.leRange.cacher() #on cache le range car on construit la tour
        self.aPlacer = None #on efface les objets temporaires
        self.aPlacerVue = None
        self.interface.zoneJeu.config(cursor="") #on reset le curseur
        
        #enlever les objets temporaires de la liste
        self.lesTours = self.lesTours[:-1]
        self.lesToursVue = self.lesToursVue[:-1]
        
        #on recule d'un id
        self.idTour = self.idTour - 1
        
    def deplacerObjets(self, event): #deplacer les objets temporaire (quand la tour flotte sous la souris pour la construire)
        self.interface.zoneJeu.config(cursor="cross")
        self.aPlacer.x = event.x
        self.aPlacer.y = event.y
        
        self.aPlacerVue.leRange.cacher() #pour bouger/actualiser
        self.aPlacerVue.leRange.affichage()
        
        self.aPlacerVue.cacher()
        self.empVal = self.laMap.emplacementValide(event.x, event.y) #est-ce un emplacement valide sur la map?
        self.aPlacerVue.affichage(valide=self.empVal)


    def selectionTour(self,event):
        lesObjets = self.interface.zoneJeu.find_overlapping(event.x-10, event.y-10, event.x+10, event.y+10) #liste des objets sous la souris
        found = False #est-ce qu'on a clique sur une tour?
        
        for i in lesObjets:
            lesTags = self.interface.zoneJeu.gettags(i)
            if len(lesTags) > 0: #protection contre objet none
                if lesTags[0] == "Tour": #on regarde si l'objet en cours est une tour
                    if self.tourSelect != None: #on doit deselectionner la tour actuelle ou popper le menu d'upgrade si c'est la meme tour
                        if int(lesTags[1]) == self.tourSelect.idTour: #si tour deja selectionnee, on ouvre le menu d'upgrade
                                self.interface.unPopup = PopupUpgradeTour(leCanvas=self.interface.zoneJeu, x=350, y=100, leController=self, idTour = self.tourSelect.idTour) #popper fenetre
                        else: #si une autre tour, on deselectionne
                            self.getInfoTourVue(self.tourSelect.idTour).leRange.cacher()  #cacher range de l'ancienne tour
                            self.tourSelect = self.getInfoTour(int(lesTags[1]))  #afficher autre tour
                            self.getInfoTourVue(self.tourSelect.idTour).leRange.affichage() 
                            self.getInfoTourVue(self.tourSelect.idTour).affichage(True) #pour pas etre cache par le range  
                    else: #si aucune tour selectionnee auparavant, on en selectionne une
                        self.tourSelect = self.getInfoTour(int(lesTags[1]))  #la tour cliquee devient la tour selectionnee
                        self.getInfoTourVue(self.tourSelect.idTour).leRange.affichage() 
                        self.getInfoTourVue(self.tourSelect.idTour).affichage(True) #pour pas etre cache par le range  
                        
                    found = True #on a clique sur une tour
                elif lesTags[0] == "Creep": #on choisi une cible
                    if self.tourSelect != None:
                        self.tourSelect.cible = self.getInfoCreep(int(lesTags[1])) #donner la priorite a ce creep
                        #print self.tourSelect.cible.idCreep #debug
                        found = True
                    
        
        if found == False: #pas clique sur une tour ou creep = deselectionner tour
            if self.tourSelect != None:
                self.getInfoTourVue(self.tourSelect.idTour).leRange.cacher()
            self.tourSelect = None
            self.interface.zoneJeu.config(cursor="")
        else: #si on a selectionne quelque chose
            self.interface.zoneJeu.config(cursor="cross")

         
#########
if __name__ == "__main__": 
    test=Controller()