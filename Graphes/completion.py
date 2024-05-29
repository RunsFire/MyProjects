import Automates
import copy
from utilitaire import *
from fonctions_auto import *
from determinisation import *

# Fichier contenant les fonctions liées à la complétion d'un automate

def complet(auto: dict) -> bool :
    '''Renvoie si l'automate est complet ou non (True ou False)'''
    exist = set()
    for transi in auto["transitions"] :
        exist.add((transi[0], transi[1]))   # Ajoute toutes les transitions dans un set (état de départ + lettre)

    for etat in auto["etats"] :             # Vérifie si chaque état possède bien une transition avec chaque lettre de l'alphabet
        for lettre in auto["alphabet"] :
            if (etat, lettre) not in exist :
                return False
    return True



def complete(automate: dict) -> dict :
    '''Renvoie un automate complété de celui donné en paramètre'''
    if complet(automate) : return automate
    auto = copy.deepcopy(automate) 
    transis_compl = list()
    puit = sorted(auto["etats"])[-1]+1  # On prend l'état original ayant la plus haute valeur, et l'état puit est cette valeur +1
    auto["etats"].append(puit)
    exist = set()       # Set qui garde les transitions existantes
    for transi in auto["transitions"] :
        exist.add((transi[0], transi[1]))       # Ajoute toutes les transitions dans un set (état de départ + lettre)
        transis_compl.append(transi)            # liste à part pour pouvoir itérer plus simplement (utilisé aussi dans la prochaine boucle, et est assigné à la fin de la fonction)
    
    
    for etat in auto["etats"] :
        for lettre in auto["alphabet"] :
            if (etat, lettre) not in exist :    # Si la transition qui part d'un état E et où on lit la lettre L n'existe pas, alors on la crée, avec comme état où on arrive l'état puit
                transis_compl.append([etat, lettre, puit])
    
    auto["transitions"] = transis_compl
    return auto



def complement(auto: dict) -> dict :
    '''Renvoie le complément de langage accepté par l'automate donné en paramètre'''
    auto_complet = complete(renommage(determinise(auto)))       # Pour avoir le complément, il faut avoir un automate complet et déterministe
    auto_complement = {"alphabet" : auto_complet["alphabet"][:], "etats" : auto_complet["etats"][:], "transitions" : auto_complet["transitions"][:], "I" : auto_complet["I"][:], "F" : list()}
    for etat in auto_complet["etats"] :         # On itère sur tous les états qui existent
        if etat not in auto_complet["F"] :      # Si in état sur lequel on itère n'est pas dans l'automate original,
            auto_complement["F"].append(etat)   # On le met comme état terminal dans la copie

    return auto_complement



if __name__ == "__main__" :
    print(complet(Automates.auto0))
    print(complet(Automates.auto1))
    print(complete(Automates.auto0))
    print(complement(Automates.auto3))
    print()
    print(renommage(determinise(complete(Automates.auto21))))
    print(complement(Automates.auto26)) #e ex 3 TD3