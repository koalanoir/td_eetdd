
from ast import And
from asyncio.windows_events import NULL
from platform import machine
from ressourceInfinie import *
from ressourceStockee import *

class Machine:
    """
        simple machine à café
    """

    def __init__(self):
        self._nombreCafesServis = 0
        self._argentEncaisse = 0
        self._boutonSucreAppuye=False
        self._gobelets= RessourceStockee(1)
        self._cafe=RessourceStockee(1)
        self._sucre=RessourceStockee(1)
        self._eau=RessourceInfinie(True)
        self._modulePrelevementAutomatique=NULL

    def Machine(self,module):
        self._modulePrelevementAutomatique=module

    def PeutFaireUnCafeSimple( self,somme):
        return somme >= 0.4 and self._eau.estPresente() and self._gobelets.estPresente() and self._cafe.estPresente()

    def PeutFaireUnCafeSucre(self, somme):
        return self.PeutFaireUnCafeSimple(somme) and self._sucre.estPresente()
    
    def Insérer(self, somme,avecMug):
        if(self.PeutFaireUnCafeSimple(somme)):
            self._argentEncaisse += somme
            self._nombreCafesServis +=1
            self._cafe.Consommer()
            if not avecMug:
                self._gobelets.Consommer()
            if self._boutonSucreAppuye and self.PeutFaireUnCafeSucre(somme):
                self._sucre.Consommer() 
        self._boutonSucreAppuye = False

            

    def GetNombreCafésServis(self):
        return self._nombreCafesServis

    
    def GetArgentEncaissé(self):
        return self._argentEncaisse

    def GetStockSucre(self):
        return self._sucre.GetStock()
    
    def couperEau(self):
        self._eau= RessourceInfinie(False)
    
    def sucreCafe(self):
        self._boutonSucreAppuye=True

    def ReapprovisionnerCafe(self):
        self._cafe.Réapprovisionner()

    def ReapprovisionnerGobelet(self):
        self._gobelets.Réapprovisionner()
    

    def ReapprovisionnerSucre(self) :
        self._sucre.Réapprovisionner()
    

    def PayerEnCB(self) :
        somme = 0.40
        paiementRéussi = self._modulePrelevementAutomatique.Prelever(somme);
        if (paiementRéussi):
            self.Insérer(somme)
     

    