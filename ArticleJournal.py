from Document import Document
import Data
class ArticleJournal(Document):
    def __init__(self, titre, ISBN, nbrPages, datePublication, journal):
        super().__init__(titre, ISBN, nbrPages)
        self.datePublication = datePublication
        self.journal = journal
        Data.DictionnaireDocuments[titre] = ISBN

# Alternative method to use the super() function
# I create a seperate and independant Document object before creating a ArticleJournal object
# class ArticleJournal2(Document):
#     def __init__(self, doc, datePublication, journal):
#         super().__init__(doc.titre, doc.ISBN, doc.nbrPages)
#         self.datePublication = datePublication
#         self.journal = journal


