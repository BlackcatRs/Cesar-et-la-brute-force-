#!/usr/bin/env python3

from OutilsCrypto import *

txt="BONJOUR"
clef=3


def Ecesar(txt, clef, paq=1) :
    list = []
    var=paquet(txt, 1)
    for valeur in var.values():
        valeur += clef
        valeur %= mod2base(paq)
        list.append(xedoc(valeur))

    txtCodee = ""
    for value in list:
        txtCodee += value

    return txtCodee



print("Voila votre text <<", txt,">> codee par paquet de 1 : ", Ecesar(txt, clef))
