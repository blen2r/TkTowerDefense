########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Vue           #
# Proprietaire: PE     #
########################

#imports
from Tkinter import *
from tkFont import *
from Popup import *
from VueJeu import *
#from Controller import *
from CallbackComplexe import *

class Vue:
    def __init__(self, leController=None):
        #on doit initialiser tkinter
        self.hauteur = 600
        self.largeur = 800
        self.root = Tk()
        self.root.title("Tower Defense Beta")
        self.root.config(background="black")
        self.root.geometry("%dx%d%+d%+d" % (self.largeur, self.hauteur, 0, 0)) #taille fenetre
        
        self.leController=leController
        
        #on s'occupe des canvas
        self.skin = None #skin a appliquer aux canvas
        self.zoneAchat = None
        self.zoneJeu = None
        self.zoneVie = None
        self.menu = None #ecran du menu
        self.scores = None #ecran de scores
        
        #on remplit les canvas
        self.configMenu()
        self.configScores()
        #pas jeu car les parametres sont determines par un popup
        
        #un popup maximum a la fois
        self.unPopup = None
        
        
    ####menu
    def chargerMenu(self):
        self.menu.place(x=0, y=0, anchor=NW)
    
    def dechargerMenu(self):
        self.menu.place_forget()
        
    def configMenu(self):
        #fond
        self.menu = Canvas(self.root, width=self.largeur, height=self.hauteur, bg="black", highlightthickness=0)
        self.imageMenu = PhotoImage(file="Menu/fondMenu.gif")
        self.fondMenu = self.menu.create_image(0, 0, anchor=NW, image=self.imageMenu)
        
        #boutons
        self.imNouvPartie = PhotoImage(file="Menu/butNouvPartie.gif")
        nouvPartie = Button(master=self.menu, image=self.imNouvPartie, command=self.nouvellePartie)
        nouvPartie.place(x=self.largeur/2, y=70, anchor=N)
        
        self.imScores = PhotoImage(file="Menu/butScores.gif")
        butScores = Button(master=self.menu, image=self.imScores, command=self.voirScores)
        butScores.place(x=self.largeur/2, y=240, anchor=N)
        
        self.imQuitter = PhotoImage(file="Menu/butQuitter.gif")
        butQuitter = Button(master=self.menu, image=self.imQuitter, command=sys.exit)
        butQuitter.place(x=self.largeur/2, y=410, anchor=N)
    
    
    ####jeu
    def chargerJeu(self):
        #placer les 3 canvas (jeu, achat et vie)
        self.zoneJeu.place(x=0, y=0, anchor=NW)
        self.zoneAchat.place(x=700, y=0, anchor=NW)
        self.zoneVie.place(x=0, y=500, anchor=NW)
    
    def dechargerJeu(self):
        #on fait disparaitre les 3 canvas
        self.zoneJeu.place_forget()
        self.zoneAchat.place_forget()
        self.zoneVie.place_forget()
        
    def configJeu(self):
        self.skin = self.skin+"/" #repertoire des images
        self.boutonsJeu = [] #les boutons d'achat de tours
        
        #canvas
        self.zoneJeu = Canvas(self.root, width=700, height=500, highlightthickness=0)
        self.zoneAchat = Canvas(self.root, width=100, height=500, highlightthickness=0)
        self.zoneVie = Canvas(self.root, width=800, height=100, highlightthickness=0)
        
        #fonds
        self.imageAchat = PhotoImage(file=self.skin+"zoneAchat.gif")
        self.fondAchat = self.zoneAchat.create_image(0, 0, anchor=NW, image=self.imageAchat)
        
        self.imageVie = PhotoImage(file=self.skin+"zoneVie.gif")
        self.fondVie = self.zoneVie.create_image(0, 0, anchor=NW, image=self.imageVie)
        
        #Le jeu est gere dans une classe a part pour des fins de lisibilite
        self.jeu = VueJeu(leController=self.leController, zoneJeu=self.zoneJeu, laVue=self)
        
        #Boutons
        self.imTour = PhotoImage(file=self.skin+"butTour.gif")
        nomsBoutons = self.leController.listeTypesTours() #on demande au controller une liste de tous les types de tours existants
        espace=70 #espace entre chaque bouton
        compte=0 #iterateur pour la liste
        
        for i in nomsBoutons:
            call = CallbackComplexe(self.leController.choisirLevelTour, i) #chaque bouton va appeler la meme commande mais avec des param. differents
            self.boutonsJeu.append(Button(master=self.zoneAchat, image=self.imTour, command=call)) #on rajoute un nouveau bouton a la liste, avec sa commande personelle
            self.boutonsJeu[compte].place(x=100/2, y=10+compte*espace, anchor=N) #on affiche ce bouton
            compte = compte+1 #on incremente compte
            
            
        #vie et argent
        self.argentReste = StringVar()
        self.argentReste.set("$$$: "+str(self.leController.getInfoJoueur().argent))
        
        self.vie = Label(self.zoneVie, text="Vie:", foreground="green", background="black", font=Font(size=14))
        self.vie.place(x=50, y=40, anchor=NW)
        self.vieVert = self.zoneVie.create_rectangle(90, 45, 90+self.leController.getInfoJoueur().ptsDeVie*2, 65, fill="green", outline="white")
        self.vieRouge = self.zoneVie.create_rectangle(90+self.leController.getInfoJoueur().ptsDeVie*2, 45, 290, 65, fill="red", outline="white")
        self.argent = Label(self.zoneVie, textvariable=self.argentReste, foreground="green", background="black", font=Font(size=14))
        self.argent.place(x=470, y=40, anchor=NW)

    
    ####highscore
    def chargerScores(self):
        lesNoms, lesPoints = self.leController.lesScores.afficherScore()
        lesLabels = []
        
        
        compte = 0
        for i in lesNoms:
            if compte < 3:
                lesLabels.append( Label(self.scores, text=i+"\t"+str(lesPoints[compte]), foreground="green", background="black", font=Font(size=16) ))
                lesLabels[compte].place(x=340, y=100+100*compte, anchor=NW)
                compte = compte + 1
        
        self.scores.place(x=0, y=0, anchor=NW)
    
    def dechargerScores(self):
        self.scores.place_forget()
        
    def configScores(self):
        #fond
        self.scores = Canvas(self.root, width=self.largeur, height=self.hauteur, bg="black", highlightthickness=0)
        self.imageScores = PhotoImage(file="Menu/fondMenu.gif")
        self.fondScores = self.scores.create_image(0, 0, anchor=NW, image=self.imageScores)
        
        #afficher les scores avec la classe a Yann
        
        
        #bouton pour retourner au menu
        self.imOkay = PhotoImage(file="Menu/butOkay.gif")
        butOkay = Button(master=self.scores, image=self.imOkay, command=self.cacherScores)
        butOkay.place(x=self.largeur/2, y=480, anchor=N)


    ####fonctions des boutons du menu
    def nouvellePartie(self):
        self.leController.nbrParties = self.leController.nbrParties + 1
        if self.leController.nbrParties > 1:
            self.leController.reset()
        #generer un popup
        self.unPopup = PopupChoixSkin(laVue=self, leCanvas=self.menu, x=self.largeur/2, y=150)
            
    def voirScores(self):
        self.dechargerMenu()
        self.chargerScores()
        
    def cacherScores(self):
        self.dechargerScores()
        self.chargerMenu()
    
    def actualiserVieArgent(self):
        self.zoneVie.delete(self.vieVert)
        self.vieVert = self.zoneVie.create_rectangle(90, 45, 90+self.leController.getInfoJoueur().ptsDeVie*2, 65, fill="green", outline="white")
        self.zoneVie.delete(self.vieRouge)
        self.vieRouge = self.zoneVie.create_rectangle(90+self.leController.getInfoJoueur().ptsDeVie*2, 45, 290, 65, fill="red", outline="white")
        
        self.argentReste.set("$$$: "+str(self.leController.getInfoJoueur().argent))
