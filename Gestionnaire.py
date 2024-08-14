from Personne import Personne
import Data
class Gestionnaire(Personne):
    def __init__(self, nom, prenom, DOB, numGestionnaire):
        super().__init__(nom, prenom, DOB)
        self.numGestionnaire = numGestionnaire
        Data.DictionnaireGestionnaires[nom] = prenom
