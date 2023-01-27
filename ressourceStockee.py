from ressource import Ressource
class RessourceStockee(Ressource):
    def __init__(self,stockInitial):
        self._stock=stockInitial

    def Consommer(self):
        super().Consommer()
        self._stock-=1

    def Réapprovisionner(self):
        self._stock+=1

    def estPresente(self):
        super().estPresente()
        return self._stock>0
    
    def GetStock(self):
        return self._stock
