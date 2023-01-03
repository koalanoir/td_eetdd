
from platform import machine


class Machine:
    """
        simple machine à café
    """

    def __init__(self,nombreGobeletsInitial, dosesCaféInitiales):
        self._nombreCafésServis = 0
        self._argentEncaissé = 0
        self._nombreCafésServis = 0
        self._argentEncaissé = 0
        self._eauDisponible = True
        self._gobeletsDisponibles = nombreGobeletsInitial
        self._caféEnStock = dosesCaféInitiales

    def Insérer(self, somme,avecMug):
        if(somme == 0.4 and self._eauDisponible and (self._gobeletsDisponibles>0 or avecMug) and self._caféEnStock):
            self._argentEncaissé += 0.4
            self._nombreCafésServis +=1
            if not avecMug:
                self._gobeletsDisponibles -=1 
            self._caféEnStock -=1
            

    def GetNombreCafésServis(self):
        return self._nombreCafésServis

    
    def GetArgentEncaissé(self):
        return self._argentEncaissé

    def GetNombreGobelet(self):
        return self._gobeletsDisponibles

    def CouperEau(self):
        self._eauDisponible=False

    def CouperCafe(self):
        self._caféEnStock=0
        
    def PlusDeGobelet(self):
        self._gobeletsDisponibles=0
        

    