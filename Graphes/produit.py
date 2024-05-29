from fonctions_auto import *
from determinisation import *
import Automates

# Fichier contenant les fonctions liées au produit de deux automates (incluant dont l'intersection et la différence)
# On part ici du principe que les deux automates ont déjà le même alphabet. Sinon, il aurait suffit de faire une vérification de cette condition au début de produit.

def inter(auto1: dict, auto2: dict) -> dict :
    '''Renvoie l'intersection de deux automates'''
    auto1v = renommage(determinise(auto1))
    auto2v = renommage(determinise(auto2))
    prod = produit(auto1v,auto2v)
    # On ajoute un état comme terminal si les deux états qui le compose sont finaux dans les deux automates originaux.
    prod["F"] = [(x, y) for (x, y) in prod["etats"] if x in auto1["F"] and y in auto2["F"]] 
    return prod



def difference(auto1: dict, auto2: dict) -> dict :
    '''Renvoie la différence de deux automates'''
    auto1v = renommage(determinise(auto1))
    auto2v = renommage(determinise(auto2))
    prod = produit(auto1v,auto2v)
    # On ajoute un état comme terminal si le premier état qui le compose est final (dans le premier automate) et le second ne l'est pas (dans le second automate).
    prod["F"] = [(x, y) for (x, y) in prod["etats"] if x in auto1["F"] and y not in auto2["F"]] 
    return prod



def produit(auto1 : dict, auto2: dict) -> dict :
    '''Automate intermédiaire permettant de réaliser les procédés communs aux deux autres fontions'''
    autoprod = dict()
    autoprod["I"] = [(un, deux) for un in auto1["I"] for deux in auto2["I"]]    # Utilise cette méthode pour ne pas avoir un tuple de liste (càd | 'I': [(0, 0)] | et non | 'I': [([0], [0])] |)
    autoprod["alphabet"] = auto1["alphabet"][:]
    autoprod["etats"], autoprod["transitions"] = list(), list()
    
    etatsAVerif = [(etat1,etat2) for etat1 in auto1["I"] for etat2 in auto2["I"]]   # états restants à traiter 
    etatsVisites = set(etatsAVerif)     # savoir quels etats ont déjà été traité

    while etatsAVerif :     # Tant qu'il reste des états à traiter ...
        (x, y) =  etatsAVerif.pop()         # un tuple, (x, y), prend la valeur de l'état qui a été retiré de la liste des états à vérifer
        autoprod["etats"].append((x, y))    # rajoute ce couple à la liste des états qui composent l'automate produit
        
        for lettre in autoprod["alphabet"] :    # pour chaque lettre de l'alphabet ...
            # ... on récupère les états de chaque automate où l'on peut arriver en lisant cette lettre
            etats1 = lirelettre(auto1["transitions"], [x], lettre)
            etats2 = lirelettre(auto2["transitions"], [y], lettre)
            for a in etats1 :       # On parcours ensuite les deux listes obtenues ...
                for b in etats2 :
                    nvl_etat = (a, b)
                    autoprod["transitions"].append([(x, y), lettre, nvl_etat])      # ... et on rajoute la transitio à l'automate produit
                    if nvl_etat not in etatsVisites :       
                        # Si l'état n'est pas dans la liste de ceux visités, on l'ajoute à cette lsite ainsi que dans les états à vérifier.
                        etatsAVerif.append(nvl_etat)
                        etatsVisites.add(nvl_etat)

    return autoprod


    

if __name__ == "__main__" :
    auto4 =  Automates.auto4
    auto5 = Automates.auto5
    print(inter(auto4,auto5))
    print(renommage(inter(auto4,auto5)))
    print("TD4 ex2 -> 3")
    auto = {
    "alphabet": ['a', 'b'],
    "etats": [0, 1],
    "transitions": [[0, 'a', 0], [0, 'b', 1], [1, 'a', 1], [1, 'b', 0]],
    "I": [0],
    "F": [1]}

    auto2 = {
    "alphabet": ['a', 'b'],
    "etats": [2, 3, 4, 5],
    "transitions": [[2, 'a', 3], [2, 'b', 2], [3, 'a', 4], [3, 'b', 3], [4, 'a', 5], [4, 'b', 4], [5, 'a', 5], [5, 'b', 5]],
    "I": [2],
    "F": [4]}
    print()
    print()
    print(inter(auto, auto2))
