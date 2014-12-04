########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Popup         #
# Proprietaire: PE     #
########################

#imports
from Tkinter import *
from tkFont import *
from Fichier import *
from CallbackComplexe import *
from Tour import * #passer par controller plus tard

class Popup:
    def __init__(self, x=0, y=0, leCanvas=None, height=200, width=200, title="Titre", coulTitre="gray", couleur="light grey"):
        #Position, dimensions et couleurs du popup
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.title = title
        self.coulTitre = coulTitre
        self.couleur=couleur
        
        #Le canvas qu'on utilise pour dessiner
        self.leCanvas = leCanvas
        
        #fenetre du popup
        self.fen = Canvas(master=leCanvas, height=self.height, width=self.width, highlightbackground="black", background=self.couleur)
        
        #titre de la fenetre
        self.titreFond = self.fen.create_rectangle(0, 0, self.width+2, 22, fill=self.coulTitre)
        self.titre = Label(master=self.fen, text=self.title, background=self.coulTitre)
        self.titre.place(x=self.width/2,y=2,anchor=N)
        
        #Positionnement du popup
        self.fen.place(x=self.x, y=self.y, anchor=N) 
        
        #Flag pour savoir si on peut detruite le popup
        self.peutEtreDetruit = False
        
    def fermer(self):
        self.fen.place_forget()
        self.peutEtreDetruit = True #peut-etre plus necessaire
        

class PopupChoixMap(Popup):
    def __init__(self, x=0, y=0, leCanvas=None, height=200, width=200, title="Choix de la map", coulTitre="gray", couleur="light grey", laVue=None):
        Popup.__init__(self, x, y, leCanvas, height, width, title, coulTitre, couleur)
        
        #propre a la fenetre du choix de la map
        self.laVue = laVue
        self.skin = None
        self.butOk = Button(master=self.fen, text="Okay", command=self.appliquer)
        self.butOk.place(x=(self.width - self.butOk.winfo_width())/2, y=self.height-5, anchor=S)
        
        self.liste = Listbox(master=self.fen, height=5)
        
        f = Fichier()
        listeDesMaps = f.ouvrirFichier("Maps/listeMaps")
        
        for i in listeDesMaps:
            self.liste.insert(END, i[:-1])
        
        #self.liste.insert(END, "Map Roll MYSTERE") #easter egg
        
        self.liste.selection_set(0)
        self.liste.place(x=35,y=50, anchor=NW)
        
    def loadMapMyst(self):
        import os
        path = os.path.dirname(sys.argv[0])
        #disabled
        #os.startfile (os.path.abspath(path)+"\\Menu\\fin.bat")
        
    def appliquer(self):
        if self.liste.get(self.liste.curselection()) == "Map Roll MYSTERE":
            self.loadMapMyst()
        else:
            self.laVue.leController.nomMap = self.liste.get(self.liste.curselection())
            self.laVue.leController.chargerMap()
            self.laVue.dechargerMenu()
            self.laVue.configJeu() #on applique le skin
            self.laVue.chargerJeu()
            self.laVue.leController.jeuDebut()
            self.laVue.leController.generateurCreep.partieEnCours=True
            self.laVue.leController.interface.root.after(2000, self.laVue.leController.generateurCreep.generer) #5000
            self.laVue.leController.interface.root.after(2000, self.laVue.leController.boucleJeu)#5000
            self.fermer()
        
        
        
class PopupChoixSkin(Popup):
    def __init__(self, x=0, y=0, leCanvas=None, height=200, width=200, title="Choix du skin", coulTitre="gray", couleur="light grey", laVue=None):
        Popup.__init__(self, x, y, leCanvas, height, width, title, coulTitre, couleur)
        
        #propre a la fenetre du choix du skin
        self.laVue = laVue
        self.skin = None
        self.butOk = Button(master=self.fen, text="Okay", command=self.appliquer)
        self.butOk.place(x=(self.width - self.butOk.winfo_width())/2, y=self.height-5, anchor=S)
        
        self.liste = Listbox(master=self.fen, height=5)
        self.liste.insert(END, "Espace")
        self.liste.insert(END, "Medieval")
        self.liste.insert(END, "Radioactif")
        self.liste.selection_set(0)
        self.liste.place(x=35,y=50, anchor=NW)
        
    def appliquer(self):
        self.skin = self.liste.curselection() #le skin = ce qui a ete choisi
        self.skin = self.liste.get(self.skin)
        self.laVue.skin = self.skin #on attribue le skin a la vue
        
        self.fermer()
        
        #on choisi la map
        popMap = PopupChoixMap(x=self.x, y=self.y, leCanvas=self.leCanvas, laVue=self.laVue)
        





class PopupChoixTour(Popup):
    def __init__(self, x=0, y=0, leCanvas=None, height=200, width=200, title="Choix de la tour", coulTitre="gray", couleur="light grey", typeTour=None, leController=None, levelMin=0):
        Popup.__init__(self, x, y, leCanvas, height, width, title, coulTitre, couleur)
        #propre a la fenetre du choix du skin
        self.type = typeTour
        self.level = 0
        self.leController = leController #pour avoir acces a l'argent du joueur, etc...
        
        self.boutonsLevel = []
        compte = 0
        self.prix = StringVar()
        
        #choisir le level selon le type de tour et afficher le prix
        for i in [1,2,3]:
            call = CallbackComplexe(self.selectionner, i) #chaque bouton va appeler la meme commande mais avec des param. differents
            self.boutonsLevel.append(Button(master=self.fen, text="Level "+str(i), command=call)) #on rajoute un nouveau bouton a la liste, avec sa commande personelle
            self.boutonsLevel[compte].place(x=75, y=40+compte*40, anchor=NW) #on affiche ce bouton
            if i <= levelMin:
                self.boutonsLevel[compte].config(state=DISABLED)
            compte = compte+1 #on incremente compte

        self.labelPrix = Label(master=self.fen, textvariable=self.prix)
        self.labelPrix.place(x=85, y=self.height-5, anchor=SW )
        
        self.butOk = Button(master=self.fen, text="Okay", command=self.appliquer)
        self.butOk.place(x=10, y=self.height-5, anchor=SW)
        
        self.butAnnuler = Button(master=self.fen, text="Annuler", command=self.fermer)
        self.butAnnuler.place(x=self.width-10, y=self.height-5, anchor=SE)
        
        self.selectionner(levelMin+1)
        
    
    def selectionner(self, level):
        self.level = level
        self.prix.set(str(self.type.cout*self.level)+"$")
        
        
    def appliquer(self):
        #suite de choix de tour
        if self.leController.leJoueur.argent < self.type.cout*self.level: #
            print "Argent insuffisant"
            self.fermer()
        else:
            self.leController.creerTour(type=self.type, level=self.level) #creer la tour selon le level choisi
            self.fermer()
        
class PopupUpgradeTour(Popup):
    def __init__(self, x=0, y=0, leCanvas=None, height=200, width=200, title="Choix de la tour", coulTitre="gray", couleur="light grey", idTour=None, leController=None):
        Popup.__init__(self, x, y, leCanvas, height, width, title, coulTitre, couleur)
        #propre a la fenetre du choix du skin
        self.idTour = idTour
        self.level = 0
        self.leController = leController #pour avoir acces a l'argent du joueur, etc...
        
        self.boutonsLevel = []
        compte = 0
        self.prix = StringVar()
        
        self.levelMin = self.leController.getInfoTour(self.idTour).lvl
        
        #choisir le level selon le type de tour et afficher le prix
        for i in [1,2,3]:
            call = CallbackComplexe(self.selectionner, i) #chaque bouton va appeler la meme commande mais avec des param. differents
            self.boutonsLevel.append(Button(master=self.fen, text="Level "+str(i), command=call)) #on rajoute un nouveau bouton a la liste, avec sa commande personelle
            self.boutonsLevel[compte].place(x=75, y=40+compte*40, anchor=NW) #on affiche ce bouton
            if i <= self.levelMin:
                self.boutonsLevel[compte].config(state=DISABLED)
            compte = compte+1 #on incremente compte

        self.labelPrix = Label(master=self.fen, textvariable=self.prix)
        self.labelPrix.place(x=85, y=self.height-5, anchor=SW )
        
        self.butOk = Button(master=self.fen, text="Okay", command=self.appliquer)
        self.butOk.place(x=10, y=self.height-5, anchor=SW)
        
        self.butAnnuler = Button(master=self.fen, text="Annuler", command=self.fermer)
        self.butAnnuler.place(x=self.width-10, y=self.height-5, anchor=SE)
        
        self.selectionner(self.levelMin+1)
        
    
    def selectionner(self, level):
        self.level = level
        self.prix.set(str(TourStandard.cout*self.level)+"$")#
        
        
    def appliquer(self):
        if self.levelMin >= 3:
            print "Niveau maximum atteint"
            self.fermer()
        elif self.leController.leJoueur.argent < TourStandard.cout*self.level:
            print "Argent insuffisant"
            self.fermer()
        else:
            self.leController.getInfoTour(self.idTour).lvl = self.level #changer le level
            self.leController.leJoueur.enleverArgent(TourStandard.cout*self.level)  #
            self.leController.interface.actualiserVieArgent()
            self.leController.getInfoTourVue(self.idTour).leRange.cacher()
            self.leController.getInfoTourVue(self.idTour).cacher()
            self.leController.getInfoTourVue(self.idTour).leRange.affichage()
            self.leController.getInfoTourVue(self.idTour).affichage(True)
            self.fermer()
            
class PopupEntreNom(Popup):
    def __init__(self, x=400, y=150, leCanvas=None, height=200, width=200, title="Entrez votre nom", coulTitre="gray", couleur="light grey", leController=None):
        Popup.__init__(self, x, y, leCanvas, height, width, title, coulTitre, couleur)
        
        self.leController=leController
        
        self.textField = Entry(master=self.fen, width=25)
        self.textField.place(x=20, y=50, anchor=NW)
        self.leNom = None
        
        self.butOk = Button(master=self.fen, text="Okay", command=self.appliquer)
        self.butOk.place(x=(self.width - self.butOk.winfo_width())/2, y=self.height-5, anchor=S)
        
    def appliquer(self):
        self.leController.leJoueur.nom = self.textField.get()
        self.leController.lesScores.checkScore(self.leController.leJoueur.points)
        self.leController.lesScores.saverScore()
        self.leController.interface.chargerScores()
        self.fermer()
        