import Data
class Document:
    def __init__(self, titre, ISBN, nbrPages):
        self.titre = titre
        self.ISBN = ISBN
        self.nbrPages = nbrPages
        Data.DictionnaireDocuments[titre] = ISBN

