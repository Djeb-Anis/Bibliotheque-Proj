from Personne import Personne
import Data
class Adherent(Personne):
    def __init__(self, nom, prenom, DOB, numAdherent):
        super().__init__(nom, prenom, DOB)
        self.numAdherent = numAdherent
        Data.DictionnaireAdherents[nom] = prenom
