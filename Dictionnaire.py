from Document import Document
import Data
class Dictionnaire(Document):
    def __init__(self, titre, ISBN, nbrPages, annee, maisonEdition):
        super().__init__(titre, ISBN, nbrPages)
        self.annee = annee
        self.maisonEdition = maisonEdition
        Data.DictionnaireDocuments[titre] = ISBN