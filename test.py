from main import *
import unittest
class MachineACafeTest(unittest.TestCase):
    def test_coule(self):
        #ETANT DONNE une machine
        machine =Machine()
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        sommeInsuffisante = 0.39

        #QUAND on met moins de 40cts
        machine.Insérer(sommeInsuffisante)

        # ALORS aucun café ne coule
        self.assertEqual(nombreCaféInitiaux, machine.GetNombreCafésServis())

        # ET l'argent est rendu
        self.assertEqual(argentEncaisséInitial,  machine.GetArgentEncaissé())
    
    def test_pas_d_argent(self):
        #ETANT DONNE une machine
        machine = Machine()
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