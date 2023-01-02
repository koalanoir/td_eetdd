from main import *
import unittest
class MachineACafeTest(unittest.TestCase):
    """ 
        failed
    """
    def Test_Sans_Eau(self):
        #ETANT DONNE une machine
        machine = Machine()
        machine.CouperEau()
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


    """ 
        failed
    """
    def Test_Sans_Cafe(self):
        #ETANT DONNE une machine
        machine = Machine()
        machine.CouperCafe()
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

    """ 
        failed
    """
    def test_pas_d_argent(self):
        #ETANT DONNE une machine
        machine = Machine()
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