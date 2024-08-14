from Document import Document
from Livre import Livre
from ArticleJournal import ArticleJournal
from Dictionnaire import Dictionnaire
from Adherent import Adherent
from Gestionnaire import Gestionnaire

import random

import Data

class Bibliotheque:
    def __init__(self):
        pass
    # ------------------------------------------------------------

    def ajouterAdherent(self):
        return Adherent(random.choice(Data.liste_noms), random.choice(Data.liste_prenoms), random.choice(Data.liste_DOB), random.choice(Data.liste_numAdherent))
    def supprimerAdherent(self, name_of_instance):
        for key, value in Data.DictionnaireAdherents[name_of_instance.nom]:
            Data.Archive_Adherents[key] = value
        del Data.DictionnaireAdherents[name_of_instance.nom]
        del name_of_instance
    def ajouterGestionnaire(self):
        return Gestionnaire(random.choice(Data.liste_noms), random.choice(Data.liste_prenoms), random.choice(Data.liste_DOB), random.choice(Data.liste_numGestionnaire))
    def supprimerGestionnaire(self, name_of_instance):
        for key, value in Data.DictionnaireGestionnaires[name_of_instance.nom]:
            Data.Archive_Gestionnaires[key] = value
        del Data.DictionnaireGestionnaires[name_of_instance.nom]
        del name_of_instance
# ------------------------------------------------------------

    def ajouterLivre(self):
        return Livre(random.choice(Data.liste_titres_et_auteurs_Livres), random.choice(Data.liste_ISBN), random.choice(Data.liste_nbrPages), random.choice(Data.liste_maisonEdition))
    def supprimerLivre(self, name_of_instance):
        interim_dict = {}  # Adding an intermidiary dictionnary in order to avoid RuntimeError: dictionary changed size during iteration
        for key, value in Data.DictionnaireDocuments.items():
            interim_dict[key] = value
        for key, value in interim_dict.items():
            if key == name_of_instance.titre and value == name_of_instance.ISBN:
                Data.Archive_Documents[key] = value
                del Data.DictionnaireDocuments[name_of_instance.titre]
        del name_of_instance
    def ajouterArticleJournal(self):
        return ArticleJournal(random.choice(Data.liste_titres_Journaux), random.choice(Data.liste_ISBN), random.choice(Data.liste_nbrPages), random.choice(Data.liste_DatePublication), random.choice(Data.liste_journaux))
    def supprimerArticleJournal(self, name_of_instance):
        interim_dict = {}
        for key, value in Data.DictionnaireDocuments.items():
            interim_dict[key] = value
        for key, value in interim_dict.items():
            if key == name_of_instance.titre and value == name_of_instance.ISBN:
                Data.Archive_Documents[key] = value
                del Data.DictionnaireDocuments[name_of_instance.titre]
        del name_of_instance
    def ajouterDictionnaire(self):
        return Dictionnaire(random.choice(Data.liste_titres_Dictionnaires), random.choice(Data.liste_ISBN), random.choice(Data.liste_nbrPages), random.choice(Data.liste_annees), random.choice(Data.liste_maisonEdition))
    def supprimerDictionnaire(self, name_of_instance):
        interim_dict = {}
        for key, value in Data.DictionnaireDocuments.items():
            interim_dict[key] = value
        for key, value in interim_dict.items():
            if key == name_of_instance.titre and value == name_of_instance.ISBN:
                Data.Archive_Documents[key] = value
                del Data.DictionnaireDocuments[name_of_instance.titre]
        del name_of_instance

# ------------------------------------------------------------

    def afficherDictionnaireAdherents(self):
        print(Data.DictionnaireAdherents)
    def afficherDictionnaireGestionnaire(self):
        print(Data.DictionnaireGestionnaires)
    def afficherDictionnaireDocuments(self):
        print(Data.DictionnaireDocuments)
    def afficherArchiveAdherents(self):
        print(Data.Archive_Adherents)
    def afficherArchiveGestionnaire(self):
        print(Data.Archive_Gestionnaires)
    def afficherArchiveDocuments(self):
        print(Data.Archive_Documents)
    def afficherDictionnaireEmprunts(self):
        print(Data.DictionnaireEmprunts)
    def afficherArchiveEmprunts(self):
        print(Data.Archive_Emprunts)

# ------------------------------------------------------------

    def ajouterEmprunt(self, ISBN_input):
        if ISBN_input in Data.DictionnaireEmprunts.items():
            print("Ce document est déjà emprunté")
        else:
            for key, value in Data.DictionnaireDocuments.items():
                if value == ISBN_input:
                    Data.DictionnaireEmprunts[key] = value
                    return (key,value)
    def archiverEmprunt(self, ISBN_input):
        if ISBN_input in Data.Archive_Emprunts.items():
            print("Ce document est déjà archivé")
        else:
            interim_dict = {} # Adding an intermidiary dictionnary in order to avoid RuntimeError: dictionary changed size during iteration
            for key, value in Data.DictionnaireEmprunts.items():
                interim_dict[key] = value
            for key, value in interim_dict.items():
                if value == ISBN_input:
                    Data.Archive_Emprunts[key] = value
                    del Data.DictionnaireEmprunts[key]
