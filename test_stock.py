from main import *
import unittest
class TestStocks(unittest.TestCase):
    def test_sans_eau(self):
               #ETANT DONNE une machine
        machine = Machine(1,5)
        machine.CouperEau()
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        sommeInsérée = 0.40
        
        # QUAND on met 40cts
        machine.Insérer(sommeInsérée)
        machine.Insérer(sommeInsérée)

        #ALORS un café coule
        nombreCafésFinaux = machine.GetNombreCafésServis()
        self.assertEqual(nombreCaféInitiaux + 1, nombreCafésFinaux)

        #ET l'argent est encaissé
        argentEncaisséFinal = machine.GetArgentEncaissé()
        self.assertEqual(argentEncaisséInitial + sommeInsérée, argentEncaisséFinal)

    def test_sans_cafe(self):
               #ETANT DONNE une machine
        machine = Machine(1,5)
        machine.PlusDeGobelet()
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        sommeInsérée = 0.40
        
        # QUAND on met 40cts
        machine.Insérer(sommeInsérée)

        #ALORS un café coule
        nombreCafésFinaux = machine.GetNombreCafésServis()
        self.assertEqual(nombreCaféInitiaux + 1, nombreCafésFinaux)

        #ET l'argent est encaissé
        argentEncaisséFinal = machine.GetArgentEncaissé()
        self.assertEqual(argentEncaisséInitial + sommeInsérée, argentEncaisséFinal)

    def test_sans_gobelet(self):
        #ETANT DONNE une machine
        machine = Machine(1,5)
        machine.PlusDeGobelet()
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        sommeInsérée = 0.40
        
        # QUAND on met 40cts
        machine.Insérer(sommeInsérée)

        #ALORS un café coule
        nombreCafésFinaux = machine.GetNombreCafésServis()
        self.assertEqual(nombreCaféInitiaux + 1, nombreCafésFinaux)

        #ET l'argent est encaissé
        argentEncaisséFinal = machine.GetArgentEncaissé()
        self.assertEqual(argentEncaisséInitial + sommeInsérée, argentEncaisséFinal)

if __name__ == '__main__':
    unittest.main()