########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
# Classe Score         #
# Proprietaire: JP     #
########################

from Fichier import *

class Score:
    def __init__(self, leController=None):
        self.fichier = "score" #nom du fichier au son stocker les scores
        self.load = Fichier()
        self.listeNom = [] #liste des noms du fichier
        self.listePoint = [] #liste des points associes a chaque nom du fichier
        self.leController = leController
        
    def loaderScore(self):
        self.listeNom = [] #liste des noms du fichier
        self.listePoint = [] #liste des points
        listeScore = self.load.ouvrirFichier(self.fichier)
        for i in listeScore: #rempli les listes de noms et de points en separant le fichier texte a chaque virgule
            i = i[:-1]
            entre = i.split(",")
            self.listeNom.append(entre[0])
            self.listePoint.append(int(entre[1]))
    
    def checkScore(self, score):
        self.loaderScore()
        listePointTempo = self.listePoint
        listeNomTempo = self.listeNom
        flag = False
        compte = 0
        self.listePoint = [] #liste des points de chaque joueur
        self.listeNom = [] #liste des noms du fichier
        
        for i in listePointTempo: #verifie chaque score sauvegarder et met en place le score du joueur actuel si celui-ci est assez eleve
            if score > i and flag == False:
                self.listePoint.append(score)
                self.listeNom.append(self.leController.leJoueur.nom)
                flag = True
                self.listePoint.append(i)
                self.listeNom.append(listeNomTempo[compte])
            else:
                self.listePoint.append(i)
                self.listeNom.append(listeNomTempo[compte])
            compte = compte+1
            
    def saverScore(self):
        compte = 0
        scoreAssemble = [] #liste des noms et des scores assemble avec une virgule
        for i in self.listeNom: #assemble chaque nom avec son score respectif et l'inscrit sur une ligne dans le fichier texte
            scoreAssemble.append(i+","+str(self.listePoint[compte])+'\n')
            compte = compte+1
        self.load.sauverFichier(self.fichier, scoreAssemble)
        
    def afficherScore(self):
        self.loaderScore()
        return self.listeNom, self.listePoint
    
        