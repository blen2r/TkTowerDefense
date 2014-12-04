########################
# Equipe Beta          #
# Yann David           #
# Jean-Philippe Groulx #
# Pierre-Emmanuel Viau #
#                      #
#Classe CallbckComplexe#
# Proprietaire: PE     #
#                      #
# Permet de passer des #
# parametres a une fonc#
# d'un bouton          #
########################

class CallbackComplexe:
    def __init__(self, callback, *firstArgs):
        self.__callback = callback
        self.__firstArgs = firstArgs
    
    def __call__(self, *args):
        return self.__callback (*(self.__firstArgs + args))