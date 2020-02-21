#!/usr/bin/env python3

from OutilsCrypto import *

txt="bonjour"
clef=3


def Ecesar(txt, clef, paq=2) :
    list = [] #pour stocker les resultat a la fin
    list1 = []

    dic=paquet(txt, paq) #transformer le txt en dic

    #transformer le dic en list
    for value in dic.values():
        list.append(value)
    print(list)

    #ajouter la clef
    compteur=0
    for value in list:
        list[compteur]+=clef
        compteur+=1

    #transformer les int dans la list en str
    for value in list:
        list1.append(str(value))

    #ajouter les 0 pour creer les paquet
    compteur=0
    for value in list1:
        if len(value) < paq*2:
            list1[compteur]='0'+value
        compteur=+1
    print(list1)

    for value in list1:
        print(value[0:2])
        for value in range(2):
            print(xedoc(int(value[0:2])))


    return list1


#print("Voila votre text <<", txt,">> codee par paquet de 1 : ", Ecesar(txt, clef))
Ecesar(txt,clef)
