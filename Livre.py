from Document import Document
import Data
class Livre(Document):
    def __init__(self, titre, ISBN, nbrPages, maisonEdition):
        super().__init__(titre, ISBN, nbrPages)
        self.maisonEdition = maisonEdition
        Data.DictionnaireDocuments[titre] = ISBN


