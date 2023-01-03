from main import *
import unittest
class TestMug(unittest.TestCase):
    def test_mug_detect_avec_gobelet(self):
        #ETANT DONNE une machine
        machine = Machine(1,1)
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        nombreGobeletInitiaux=machine.GetNombreGobelet()
        sommeInsérée = 0.40
        
        # QUAND on met 40cts
        machine.Insérer(sommeInsérée,True)

        #ALORS un café coule
        nombreCafésFinaux = machine.GetNombreCafésServis()
        self.assertEqual(nombreCaféInitiaux + 1, nombreCafésFinaux)

        #ET l'argent est encaissé
        argentEncaisséFinal = machine.GetArgentEncaissé()
        self.assertEqual(argentEncaisséInitial + sommeInsérée, argentEncaisséFinal)

        #Aucun Gobelet n'est utilisé
        nombreGobeletFinaux=machine.GetNombreGobelet()
        self.assertEqual(nombreGobeletInitiaux, nombreGobeletFinaux) 

    def test_mug_detect_sans_gobelet(self):
        #ETANT DONNE une machine
        machine = Machine(1,5)
        machine.PlusDeGobelet()
        nombreCaféInitiaux = machine.GetNombreCafésServis()
        argentEncaisséInitial = machine.GetArgentEncaissé()
        sommeInsérée = 0.40
       
        # QUAND on met 40cts
        machine.Insérer(sommeInsérée,True)

        #ALORS un café coule
        nombreCafésFinaux = machine.GetNombreCafésServis()
        self.assertEqual(nombreCaféInitiaux + 1, nombreCafésFinaux)

        #ET l'argent est encaissé
        argentEncaisséFinal = machine.GetArgentEncaissé()
        self.assertEqual(argentEncaisséInitial + sommeInsérée, argentEncaisséFinal)

 
if __name__ == '__main__':
    unittest.main()