# GESTION DE PROJET 
# TP1
# CLASSE Fichier
# FAIT PAR: PE
# SYLVAIN DESROCHES
# Pierre-Emmanuel Viau
# Charles Chalifoux
# Maxime Parisien


class Fichier:  
    def __init__(self):
        pass
    
    def ouvrirFichier(self, nomFiche):
        fiche = file(nomFiche+".txt")
        donnees = fiche.readlines()
        fiche.close()
        return donnees
    
    def sauverFichier(self, nomFiche, donnees):
        fiche = file(nomFiche+".txt","w")
        
        for i in donnees:
            fiche.write(i)
        
        fiche.close()