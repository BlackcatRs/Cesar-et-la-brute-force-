#!/usr/bin/env python3

from OutilsCrypto import *

txt="bonjourz"
clef=3


def Ecesar(txt, clef, paq=2) :
    list = [] #pour stocker les resultat a la fin
    list1 = []

    dic=paquet(txt, paq) #transformer le txt en dic

    for value in dic:
        print(dic(value))
    #ajouter la clef
    compteur=0
    for value in list:
        print(value)
        compteur+=1




    for value in list:
        list1.append(str(value))

    for value in list1:
        if len(value) < paq*2:
            print("value", value, "inferieur a", paq*2)
            value='0'+value
            print(value)


    return list



#print("Voila votre text <<", txt,">> codee par paquet de 1 : ", Ecesar(txt, clef))
Ecesar(txt,clef)
