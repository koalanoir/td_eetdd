
from abc import ABC, abstractmethod

class Ressource(ABC):

    @abstractmethod
    def estPresente(self): 
        pass
    @abstractmethod
    def Consommer(self): 
        pass
