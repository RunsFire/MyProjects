# Fichier contenant des fonctions générales utilisées principalement sur une String ou une liste

def pref(u: str) -> list :
    '''Renvoie la liste des préfixes du mot'''
    return list(map(lambda x: u[:x], range(len(u)+1)))



def suf(u: str) -> list :
    '''Renvoie la liste des suffixes du mot'''
    return list(map(lambda x: u[x:], range(len(u)+1)))



def fact(u: str) -> list : # L'ordre renvoyé n'est pas exactement celui de la feuille de consigne, mais je ne pense pas que cela est une réelle importance pour la suite
    '''Renvoie la liste des facteurs du mot'''
    return sorted({u[i:j] for i in range(len(u)+1) for j in range(len(u)+1) if i<=j})



def miroir(u: str) -> str :
    '''Renvoie le miroir du mot'''
    return u[::-1]      # Par compréhension : renvoie de la fin au début (-> dans le sens inverse) 



def concatene(L1: list, L2: list) -> list:
    '''Renvoie le produit de concaténation, sans doublons'''
    return sorted({(L1[i] + L2[j]) for i in range(len(L1)) for j in range(len(L2))})



def puis(L1: list, x: int) -> list:
    '''Prend un langage L et renvoie L^x'''
    L2 = L1[:]
    for i in range(x-1) :
        L2 = concatene(L1,L2)
    return L2



def tousmots(L1: list, x: int) -> list:
    '''Renvoie tous les mots de longueur <= x de l'alphabet'''
    L3, L2 = L1[:], L1[:]
    for i in range(x-1) :
        L2 = concatene(L1,L2)
        L3 += L2
    L3.append('')
    return L3



if __name__ == "__main__" :
    print(pref("coucou"))
    print(suf("coucou"))
    print(fact("coucou"))
    print(miroir("coucou"))
    L1=['aa','ab','ba','bb']
    L2=['a', 'b', '']
    print(concatene(L1, L2))
    L3=['aa','ab','bb','ba']
    print(puis(L3,2))
    print(tousmots(['a','b'],3))
    print()
    print(pref("abbab"))
    print(suf("abbab"))
    print(fact("abbab"))
    print(miroir("abbab"))