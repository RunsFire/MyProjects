import Automates
from fonctions_auto import *
from determinisation import *
from completion import *

# Fichier contenant les fonctions liées à la minimisation d'un automate

# Comparé à la déterminisation ou à la complétion, il est plus difficile de faire le test permettant de vérifier si un automate
# est un automate minimisé ou non. C'est pourquoi cette fonction n'a pas été implémentée, comme sa complexité ne serait pas très
# différente que si l'on appliquait juste la fonction de minimisation.


def minimise(auto: dict) -> dict :
    '''Renvoie l'automate minimisé de l'automate donné en paramètre.'''
    auto = complete(determinise(auto))       # Pour s'assurer que l'automate donné est déterministe et complet

    transit = dict()    # Dictionnaire, qui pour chaque état, garde l'état associé à une lettre. (utilisation de dictionnaires imbriqués pour trouver plus rapidement)

    for transi in auto["transitions"] :
        if transi[0] in transit.keys() :
            transit[transi[0]][transi[1]] = transi[2]
        else :
            transit[transi[0]] = {transi[1] : transi[2]}

    # Classe 0
    classe0 = [auto["F"][:], [i for i in auto["etats"] if i not in auto["F"]]]
    classe = moore(auto, classe0, transit)

    automate = {
        "alphabet" : auto["alphabet"][:],
        "etats" : [i for i in range(len(classe))],
        "transitions" : list(),
        "I" : list(),
        "F" : list()
    }

    etat_class = {etat: i for i, cl in enumerate(classe) for etat in cl}    # Crée un dictionnaire ayant pour clef un état et en valeur l'index de sa classe
    # ex : pour classe = [[0,1,3],[2]], on aurait etat_class = {0: 0, 1: 0, 2: 1, 3: 0}

    for clss in classe :
        prems = clss[0] # Prems est le premier chiffre de chaque classe (dans l'exemple précédent, il vaudrait donc 0 puis 2)
        for lettre in auto["alphabet"] :
            src = etat_class[prems]     # On récupère les états appartenant à un même groupe
            dest = etat_class[transit[prems][lettre]]   # On récupère les états où l'on arrive en lisant la lettre appartenant à un même groupe
            if [src, lettre, dest] not in automate["transitions"] :     # On vérifie si la transition n'a pas déjà été ajoutée
                automate["transitions"].append([src, lettre, dest])

    automate["I"] = list({etat_class[etat] for etat in auto["I"]})      # Pour éviter les erreurs (doublons), on cast en list les sets
    automate["F"] = list({etat_class[etat] for etat in auto["F"]})

    return automate


def moore(auto: dict, classe0: list, transit: dict) -> list :
    '''Applique l'algorithme de Moore et renvoie une liste contenant les différents états appartenant à la même classe.'''
    classe = classe0[:]
    while True :    # boucle infinie, dont on ne sort qu'avec un break
        nvl_classe = []     # Réinitialisation de la nouvelle classe
        for clss in classe :    # Itère sur les listes des états appartenant aux mêmes classes.
            parti = {}
            for etat in clss :
                signa = []      # signature -> permet de savoir quel lettre amène dans quel classe
                for lettre in auto["alphabet"] :
                    arrive = transit.get(etat).get(lettre)  # arrive prend comme valeur l'état A où on arrive en partant d'un état E et en lisant la lettre
                    signa.append(getindex(arrive, classe))  # on ajoute l'index à la signature
                
                signa = tuple(signa)
                if signa in parti : # Si la signature existe déjà dans les partitions (donc si un état appartient à la même classe)
                    parti[signa].append(etat)
                else :      # Sinon, on ajoute comme clef la signature, et l'état comme liste
                    parti[signa] = [etat]
        
            nvl_classe.extend(parti.values())     # On ajoute aux classes la partition
        
        if nvl_classe == classe :   # Si la classe est identique à la précédente, alors on peut s'arrêter
            break
        else :
            classe = nvl_classe[:]  # Sinon, on répète le processus
    
    return classe

def getindex(etat: int, classes: list) -> int :
    '''Renvoie l'index de la classe dans laquelle se trouve l'état - ex : classe = [[0,2,3],[1,4]] -> getindex(4, classe) renvoie 1'''
    for i, clss in enumerate(classes) : # Ajoute un index à un élément (ex : enumerate([[0,2,3],[1,4]]) va faire    [(0, [0,2,3]),(1, [1,4])]      )
        if etat in clss :
            return i

if __name__ == "__main__" :
    auto6 = Automates.auto6
    print(minimise(auto6))
    #print(renommage(minimise(auto6)))