import Bibliotheque
import Data

# ------------------------------------------------------------
# Main Code

# Création de mon objet bibliothèque
maBiblio = Bibliotheque.Bibliotheque()

print('\n------------------Ajout Adhérent------------------')
# Ajout d'un adhérent et afficher l'adhérent
adherent1 = maBiblio.ajouterAdherent()
maBiblio.afficherDictionnaireAdherents()

print('\n------------------Ajout livre------------------')
# Ajout de livres et afficher les livres
livre1 = maBiblio.ajouterLivre()
livre2 = maBiblio.ajouterLivre()
maBiblio.afficherDictionnaireDocuments()

print('\n------------------Supprimer livre------------------')
# Supprimer un livre
maBiblio.supprimerLivre(livre1)
maBiblio.afficherDictionnaireDocuments()

print('\n------------------Empreint------------------')
# Création d'un empreint et afficher l'empreint
empreint1 = maBiblio.ajouterEmprunt(livre2.ISBN)
maBiblio.afficherDictionnaireEmprunts()

print('\n------------------Archiver Empreint------------------')
# Archiver empreint et vérifier
maBiblio.archiverEmprunt(empreint1[1]) # Toujours retourner l'index [1] pour le ISBN
maBiblio.afficherArchiveEmprunts()






























