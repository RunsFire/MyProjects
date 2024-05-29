import string
import Automates

# Fichir contenant la fonction permettant de définir manuellement un automate.

def defauto() -> dict :
    ''' Définition des automates '''
    auto = dict()
    # Définition de l'alphabet
    list_alpha = list()
    alpha = ""
    print("Définissez l'alphabet de l'automate ('Next' pour terminer la saisie)\n")
    while alpha != "Next" :
        alpha = str(input("Lettre : "))
        if alpha == "Next" :
            break
        if not alpha.isalpha() :
            print("\nCaractère entré invalide -> il doit s'agir d'une (ou plusieurs) lettre.\n")
        elif alpha in list_alpha :
            print("\nLettre déjà présente dans l'alphabet.\n")
        else :
            list_alpha.append(alpha)
    auto["alphabet"] = list_alpha

    # Définition des états
    list_etat = list()
    etat = ""
    print("\nDéfinissez les états de l'automate ('Next' pour terminer la saisie)\n")
    while etat != "Next" :
        etat = str(input("Etat : "))
        if etat == "Next" :
            break
        if not etat.isnumeric() :
            print("\nCaractère entré invalide -> il doit s'agir d'un nombre.\n")
        else :
            etat = int(etat)
            if etat in list_etat :
                print("\Etat déjà présent dans la liste des états.\n")
            else :
                list_etat.append(etat)
    auto["etats"] = list_etat

    # Définition des états initiaux
    list_init = list()
    etat = ""
    print("\nDéfinissez les états initiaux de l'automate ('Next' pour terminer la saisie)\n")
    while etat != "Next" :
        etat = str(input("Etat : "))
        if etat == "Next" :
            break
        if not etat.isnumeric() :
            print("\nCaractère entré invalide -> il doit s'agir d'un nombre.\n")
        else :
            etat = int(etat)
            if etat not in list_etat :
                print("\nEtat doit avoir été déjà renseigné lors de la précédente étape.\n")
            else :
                list_init.append(etat)
    auto["I"] = list_init

    # Définition des états terminaux
    list_term = list()
    etat = ""
    print("\nDéfinissez les états terminaux de l'automate ('Next' pour terminer la saisie)\n")
    while etat != "Next" :
        etat = str(input("Etat : "))
        if etat == "Next" :
            break
        if not etat.isnumeric() :
            print("\nCaractère entré invalide -> il doit s'agir d'un nombre.\n")
        else :
            etat = int(etat)
            if etat not in list_etat :
                print("\nEtat doit avoir été déjà renseigné auparavant.\n")
            else :
                list_term.append(etat)
    auto["F"] = list_term

    # Définition des transitions
    list_transitions = list()
    etat = ""
    print("\nDéfinissez les transitions de l'automate ('Next' pour terminer la saisie)\n")
    while etat != "Next" :
        declaration = str(input("Transition (format : [etat1] [lettre] [etat2]) : "))
        if declaration == "Next" :
            break
        transi = declaration.split()
        transi[0], transi[2] = int(transi[0]), int(transi[2])
        if not ((transi[0] in auto["etats"]) and (transi[2] in auto["etats"])) :
            print("Au moins un des états n'existe pas pour cet automate.")
        elif not (transi[1] in auto["alphabet"]) :
            print("Lettre invalide.")
        elif transi in list_transitions :
            print("Transition déjà existante.")
        else :
            list_transitions.append(transi)
    auto["transitions"] = list_transitions[:]


    return auto




if __name__ == "__main__" :
    print(defauto())