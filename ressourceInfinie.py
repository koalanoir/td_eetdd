from ressource import *
class RessourceInfinie (Ressource):
    def __init__(self,estPresente):
        self._estPresente=estPresente

    def estPresente(self):
        super().estPresente()
        return self._estPresente
    
    def Consommer(self):
        return super().Consommer()