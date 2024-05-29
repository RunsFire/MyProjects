import Automates
from utilitaire import *
import copy

# Fichier contenant des fonctions générales applicables sur un automate/une partie d'un automate.

def lirelettre(transitions: list, etats: list, lettre: str) -> list:
    '''Renvoie les états où l'on peut arriver en lisant la lettre donnée en partant des états de la liste.'''
    CanGo = set()
    for transition in transitions :
        if transition[1] == lettre and transition[0] in etats :
            CanGo.add(transition[2])
    return list(CanGo)



def liremot(transitions: list, etats: list, mot: str) -> list :
    '''Renvoie les états où l'on peut arriver en lisant le mot'''
    CanGo = list(etats)
    for i in range(len(mot)) :    
        CanGo = lirelettre(transitions, CanGo, mot[i])

    return list(CanGo)



def accepte(automate: dict, mot: str) -> bool :
    '''Renvoie si le mot est accepté par l'automate'''
    return False if not liremot(automate["transitions"], automate["etats"], mot) else True



def langage_accept(auto: dict, n: int) -> list :
    '''Renvoie les mots de longeur <= n acceptés par l'automate'''
    mots = tousmots(auto["alphabet"], n)
    accept = list()
    for mot in mots :
        if (accepte(auto, mot)) :
            accept.append(mot)
    return accept



def renommage(auto: dict) -> dict:
    '''Renomme les états d'un automate'''
    etats = auto["etats"]   # Pour la suite pour avoir moins à écrire
    renomme = copy.deepcopy(auto)

    for transi in renomme["transitions"]:
        for i in range(0, 3, 2):
            for j in range(len(etats)):
                if transi[i] == etats[j]:
                    transi[i] = j

    for k in range(len(etats)):
        renomme["etats"][k] = k

    for k in range(len(auto["I"])):
        for n in range(len(etats)):
            if auto["I"][k] == etats[n]:
                renomme["I"][k] = n

    for k in range(len(auto["F"])):
        for n in range(len(etats)):
            if auto["F"][k] == etats[n]:
                renomme["F"][k] = n

    return renomme



if __name__ == "__main__" :
    auto = Automates.auto
    print(lirelettre(auto["transitions"], auto["etats"], "a"))
    print(liremot(auto["transitions"],auto["etats"],'aba'))
    print(accepte(auto, "aba"))
    print(accepte(auto, "ba"))
    print(accepte(auto, "baa"))
    print(langage_accept(auto, 3))