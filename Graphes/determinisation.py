import Automates
import copy
from utilitaire import *
from fonctions_auto import *

# Fichier contenant les fonctions liées à la déterminisation d'un automate

def deterministe(auto: dict) -> bool :
    '''Renvoie True si l'automate est déterministe, sinon False'''
    transis = set()                         # Set qui converse les transitions (état départ + lettre) déjà croisées
    for transition in auto["transitions"]:      # Parcours les transitions
        clef = (transition[0], transition[1])   # Crée un tuple composé de l'état dont on part ainsi que de la lettre qu'on lis
        if clef in transis:                 # Si le tuple est déjà dans le set, alors on renvoie False
            return False
        transis.add(clef)
    return True



def determinise(auto: dict) -> dict :
    '''Renvoie une version déterminisé de l'automate'''
    if deterministe(auto) : return auto
    
    nvls_transis = []       # Nouvelles transitions
    nvx_etats = dict()      # Nouveaux états

    cherche_transis(auto, auto["I"], nvx_etats, nvls_transis,)      # Commence à chercher les transistions à partir de l'état initial

    autodet = {
        "alphabet": auto["alphabet"][:],
        "etats": list(nvx_etats.values()),
        "transitions": nvls_transis,
        "I": [auto["I"][:]],       # un état : la liste des états initiaux
        "F": [etat for etat in nvx_etats.values() if any(e in auto["F"] for e in etat)]         # états finaux : états qui sont composés d'au moins un des états terminaux initiaux.
    }
    return autodet

def cherche_transis(auto: dict, etats: list, nvx_etats: dict, nvls_transis: list) :
    '''(Utilisé de manière récursive pour la déterminisation) Permet de chercher l'ensemble des transitions en partant d'un ensemble d'états.'''
    if tuple(etats) not in nvx_etats:       # Vérifie si l'état n'a pas déjà été exploré
        nvx_etats[tuple(etats)] = etats
        for lettre in auto["alphabet"]:     # Pour chaque lettre de l'alphabet ...
            prochain_etat = list()
            for etat in etats:          # ... on calcule le nouvel ensemble des états atteignables ...
                prochain_etat = list(set(prochain_etat + lirelettre(auto["transitions"], [etat], lettre)))

            if prochain_etat:       # ... et si cette ensemble n'est pas vide, on ajoute aux nouvelles transitions une transition partant de l'état,
                nvls_transis.append([etats, lettre, sorted(list(prochain_etat))])   # qui en lisant la lettre, arrive à l'ensemble précédemment trouvé.
                
                cherche_transis(auto, prochain_etat, nvx_etats, nvls_transis)  # Recherche récursive pour le prochain état



if __name__ == "__main__" :
    # print(deterministe(Automates.auto0))
    # print(deterministe(Automates.auto2))
    # print(determinise(Automates.auto2))
    # print(renommage(determinise(Automates.auto2)))
    # print("\nTD3 ex 1 & 2")
    # print(renommage(determinise(Automates.auto18)))
    # print()
    # print(renommage(determinise(Automates.auto19)))
    # print()
    # print(renommage(determinise(Automates.auto20)))
    # print()
    # print(renommage(determinise(Automates.auto21)))
    auto = 