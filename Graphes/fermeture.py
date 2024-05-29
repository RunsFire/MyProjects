import Automates
from utilitaire import *

# Fichier contenant les fonctions liées aux propriétés de fermeture d'un automate.
# On part du principe que les automates donnés sont déjà émondé. Comme pour le produit, dans le cas contraire, il suffirait de faire une vérification (et créer une fonction pour).

def prefixe(auto: dict) -> dict :
    '''Renvoie un automate acceptant l'ensemble des préfixes des mots du language de l'automate donné.'''
    automate = {
        "alphabet": auto["alphabet"][:],
        "etats": auto["etats"][:],
        "transitions": auto["transitions"][:],
        "I": auto["I"][:],
        "F": auto["etats"][:]          # Pour remplir la condition, il faut mettre tous les états comme terminaux
    }

    return automate



def suffixe(auto: dict) -> dict :
    '''Renvoie un automate acceptant l'ensemble des suffixes des mots du language de l'automate donné.'''
    automate = {
        "alphabet": auto["alphabet"][:],
        "etats": auto["etats"][:],
        "transitions": auto["transitions"][:],
        "I": auto["etats"][:],             # Pour remplir la condition, il faut mettre tous les états comme initiaux
        "F": auto["F"][:]         
    }

    return automate



def facteur(auto: dict) -> dict :
    '''Renvoie un automate acceptant l'ensemble des facteurs des mots du language de l'automate donné.'''
    automate = {
        "alphabet": auto["alphabet"][:],
        "etats": auto["etats"][:],
        "transitions": auto["transitions"][:],
        # Pour remplir la condition, il faut mettre tous les états comme initiaux et terminaux
        "I": auto["etats"][:],             
        "F": auto["etats"][:]          
    }

    return automate



def miroir(auto: dict) -> dict :
    '''Renvoie un automate acceptant l'ensemble des miroirs des mots du language de l'automate donné.'''
    automate = {
        "alphabet": auto["alphabet"][:],
        "etats": auto["etats"][:],
        # On change le sens des transitions ( [1, a, 2] devient [2, a, 1])
        "transitions": [[etat2, lettre, etat1] for [etat1, lettre, etat2] in auto["transitions"]],
        # On inverse les états initiaux et terminaux
        "I": auto["F"][:],             
        "F": auto["I"][:]          
    }

    return automate



if __name__ == "__main__" :
    auto = Automates.auto34
    print(prefixe(auto))
    print(suffixe(auto))
    print(facteur(auto))
    print(miroir(auto))