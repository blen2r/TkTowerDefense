########################
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
# Yann David           #
#                      #
#                      #
# Classe Map           #
# Proprietaire: Yann   #
########################

#import
from Fichier import *
from Vecteur import *
from Constantes import *

class Map:    
    def __init__(self, nomMap): #fichVect
        self.matrice = []
        f = Fichier()
        self.laMap = f.ouvrirFichier(nomMap) #liste d'entiers de la map
        self.Vecteurs = f.ouvrirFichier(nomMap+"Vect") #liste d'entiers des vecteurs
        self.vectListe = [] #vecteurs compiles
        self.emplacements = [] #matrice avec lemplacement des tours
        
        self.genererMatrice()
        self.genererVecteurs()
        self.genererEmplacements()
        
    def genererEmplacements(self): #copie la map sans les "cochonneries" (sauts de lignes, etc...)
        for i in self.laMap:
            emplacementTemp = []
            i = i[:-1]
            for j in i:
                emplacementTemp.append(int(j))
            self.emplacements.append(emplacementTemp)
            
        
    def emplacementValide(self, x, y): #regarde si le x et y sont occupes
        flag = True
        for i in range(y-25, y+25):
                for j in range(x-25, x+25):
                    xBon = j / Constantes.DIMX
                    yBon = i / Constantes.DIMY
                    if j < 680 and j > 20 and i < 490 and i > 20:        
                        if self.emplacements[yBon][xBon] != 0:
                            flag = False
                    else:
                        flag = False
                    
        return flag
        
    def changerEmplacement(self, x, y): #rendre un emplacement occupe
        xBon = x / Constantes.DIMX
        yBon = y / Constantes.DIMY
        self.emplacements[yBon][xBon] = 3
                
    
    def genererVecteurs(self): #faire la liste des vecteurs sans les cochonneries
        for i in self.Vecteurs:
            i = i[:-1]
            Coors = i.split(";")
            Coors[0] = Coors[0][:-1]
            Coors[0] = Coors[0][1:]
            PosDeb = Coors[0].split(",")
            Coors[1] = Coors[1][:-1]
            Coors[1] = Coors[1][1:]
            PosFin = Coors[1].split(",")
            self.vectListe.append( Vecteur(int(PosDeb[0]), int(PosDeb[1]), int(PosFin[0]), int(PosFin[1])) )
                                                
    
    def genererMatrice(self): #matrice sans fins de lignes
        for i in self.laMap:
            self.matrice.append(i[:-1])
        
    
    def getPosGenerateur(self): #trouver le generateur
        posX = 0
        posY = 0
        for i in self.matrice:
            for j in i:
                if j == '2':
                    return posX*Constantes.DIMX, posY*Constantes.DIMY
                posX = posX+1
            posY = posY+1
            
            
if __name__ == "__main__":
    objBase = Map(nomMap = "maps/map1")
    print objBase.emplacements
#    objBase.genererMatrice()
#    objBase.emplacementOccupe(2, 0)
#    print objBase.getPosGenerateur()
    
#    print objBase.genererMatrice()
#    objBase.genererVecteurs()
#    for i in objBase.vectListe:
#        print i.x1
#        print i.x2
#        print i.y1
#        print i.y2
#        print i.a
#        print i.b
#        print i.aUni
#        print i.bUni
#        print i.norme
    
            
            
            
            