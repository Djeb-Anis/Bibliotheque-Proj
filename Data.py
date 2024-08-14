import random
import datetime

# ------------------------------------------------------------
# Random data I need

liste_noms = [
   "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

liste_prenoms = [
    "Alice", "Bob", "Charlie", "David", "Eve",
    "Frank", "Grace", "Hannah", "Ivy", "Jack",
    "Karen", "Liam", "Mia", "Nathan", "Olivia",
    "Paul", "Quincy", "Rachel", "Steve", "Tina"
]

liste_DOB = [] # Will use random_birth_gen (DONE)
liste_numAdherent = [] # Will use random_number_Gen (DONE)
liste_numGestionnaire = [] # Will use random_number_Gen (DONE)

liste_titres_et_auteurs_Livres = [
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
    "The Catcher in the Rye by J.D. Salinger",
    "The Alchemist by Paulo Coelho",
    "Educated by Tara Westover",
]

liste_titres_Dictionnaires = [
    "Merriam-Webster's Collegiate Dictionary",
    "Oxford English Dictionary",
    "Cambridge Dictionary",
    "The American Heritage Dictionary of the English Language",
    "Collins English Dictionary",
]

liste_titres_Journaux = [
    "The Role of Social Media in Political Mobilization: A Case Study of the Arab Spring - Journal of Communication",
    "Climate Change and Its Impact on Global Food Security - Environmental Science & Policy",
    "The Effects of Sleep Deprivation on Cognitive Performance - Journal of Experimental Psychology",
    "Artificial Intelligence in Healthcare: Past, Present, and Future - Health Informatics Journal",
    "The Influence of Music on Consumer Behavior - Journal of Marketing Research",
    "Exploring the Relationship Between Mindfulness and Emotional Well-Being - Journal of Happiness Studies",
    "The Impact of Remote Work on Employee Productivity - Journal of Business Research"
]

liste_ISBN = [] # Will use random_number_Gen (DONE)
liste_nbrPages = [] # Will use random_number_Gen (DONE)

liste_DatePublication = [] # Will use random_date_gen (DONE)
liste_journaux = [
    "Springer Nature",
    "Elsevier",
    "Wiley-Blackwell",
    "Taylor & Francis",
    "SAGE Publications",
    "IEEE (Institute of Electrical and Electronics Engineers)",
    "Oxford University Press",
    "Cambridge University Press",
    "American Chemical Society (ACS)",
    "Royal Society of Chemistry (RSC)"
]
liste_annees = [] # Will use random_number_Gen (DOB)
liste_maisonEdition = [
    "Penguin Random House",
    "HarperCollins",
    "Simon & Schuster",
    "Hachette Book Group",
    "Macmillan Publishers",
    "Scholastic",
    "Bloomsbury Publishing",
    "Wiley (also a journal publisher)",
    "University of Chicago Press",
    "Knopf Doubleday Publishing Group"
]

# ------------------------------------------------------------
# Functions to generate random data

# creating a function that generates random dates
def random_date_gen(target_list, n, start_date, end_date): # We define the function with the number n of dates we want, the start and end of the time period we use to generate random dates
    delta_days = (end_date - start_date).days  # Calculate the total number of days between the two dates
    for _ in range(n):
        random_days = random.randint(0, delta_days)  # Generate a random number of days
        gen_date = start_date + datetime.timedelta(days=random_days)  # Create the random birth date
        target_list.append(str(gen_date))  # Append the date as a string to the list

# How to input the start_date and end_date
# start_date = datetime.datetime(1960, 1, 1)
# end_date = datetime.datetime(2024,1,1)


# Creating a function which will generate random numbers for my lists
def random_number_Gen(target_liste, n, start, stop):
    for _ in range(n):
        num = random.randrange(start, stop)
        target_liste.append(num)

# ------------------------------------------------------------
# Generating random data

# liste_DOB
start_date_DOB = datetime.datetime(1960, 1, 1)
end_date_DOB = datetime.datetime(2000,1,1)
random_date_gen(liste_DOB, 20, start_date_DOB, end_date_DOB)

# liste_numAdherent (6 chiffres)
random_number_Gen(liste_numAdherent,20, 100000, 999998)

# liste_numGestionnaire (3 chiffres)
random_number_Gen(liste_numGestionnaire,20, 100, 998)

# liste_ISBN (5 chiffres)
random_number_Gen(liste_ISBN,20, 10000, 99998)

# liste_nbrPages
random_number_Gen(liste_nbrPages,20, 5, 10000)

# liste_DatePublication
start_date_DatePublication = datetime.datetime(1860, 1, 1)
end_date_DatePublication = datetime.datetime(2024,1,1)
random_date_gen(liste_DatePublication, 20, start_date_DOB, end_date_DOB)

# liste_annees
random_number_Gen(liste_annees, 10, 1850, 2025)

# ------------------------------------------------------------
# Dictionnaries I need for administration

DictionnaireAdherents = {}
DictionnaireGestionnaires = {}
DictionnaireDocuments = {}
DictionnaireEmprunts = {}

Archive_Emprunts = {}
Archive_Adherents = {}
Archive_Gestionnaires = {}
Archive_Documents = {}
