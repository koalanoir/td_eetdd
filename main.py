
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
        self._gobeletsDisponibles = True
        self._caféEnStock = True

    def __init__(self):
        self._nombreCafésServis = 0
        self._argentEncaissé = 0
        self._nombreCafésServis = 0
        self._argentEncaissé = 0
        self._eauDisponible = True
        self._gobeletsDisponibles = True
        self._caféEnStock = True
    def Insérer(self, somme):
        if(somme == 0.4 and self._eauDisponible and self._gobeletsDisponibles and self._caféEnStock):
            self._argentEncaissé += 0.4
            self._nombreCafésServis +=1

    def GetNombreCafésServis(self):
        return self._nombreCafésServis

    def GetArgentEncaissé(self):
        return self._argentEncaissé

    def CouperEau(self):
        self._eauDisponible=False

    def CouperCafe(self):
        self._caféEnStock=False
        
    def PlusDeGobelet(self):
        self._gobeletsDisponibles=False
        
if __name__ == '__main__':
    machine=Machine()
    nombreCaféInitiaux = machine.GetNombreCafésServis()
    argentEncaisséInitial = machine.GetArgentEncaissé()
    sommeInsuffisante = 0.39

    #QUAND on met moins de 40cts
    machine.Insérer(sommeInsuffisante)

    # ALORS aucun café ne coule
    print(nombreCaféInitiaux)
    print(machine.GetNombreCafésServis())

    