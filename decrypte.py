#!/usr/bin/env python3

from OutilsCrypto import *


txt = input("Entrez votre texte ici : ")
paq = int(input("Entrez nobre de paquet : "))
clef = int(input("Entrez votre clef : "))

#transformer le dictionnaire en list
def dicLit(dic):
    list = []
    for value in dic.values():
        list.append(value)
    return list

#ajouter la clef a la liste
def addclef(intList, clef):
    compteur=0
    for value in intList:
        intList[compteur]+=clef
        compteur+=1

#transformer les int de la liste en str et stocker dans une autre liste "liste1"
def intStr(intList):
    list1 = []
    for value in intList:
        list1.append(str(value))
    return list1

#ajouter les 0 devant un nombre pour creer les paquet
def addpaq(strlist):
    compteur=0
    for value in strlist:
        if len(value) < paq*2:
            strlist[compteur]='0'+value
        compteur=+1

#separer les chiffre 2 par 2 et retourne une liste int
def separater(strlist, paq):
    list2 = []
    for value in strlist:
        compteur1 = 0
        compteurL = 0

        while compteur1 < paq:
            a=''
            compteur = 0
            while compteur < 2:
                a+=value[compteurL]
                compteur+=1
                compteurL+=1
            list2.append(int(a))
            compteur1+=1
    return list2

#transformer les chiffre regroupe 2 par 2 en lettre
def chiffreLettre(listInt):
    motcrypte = ''
    for element in listInt:
        motcrypte+=xedoc(element)
    return motcrypte

    return motcrypte


def Ecesar(txt, paq, clef) :

    #transformer le texte en chiffre par paquet de paq et stocker dans un dictionnaire
    dic=paquet(txt, paq)

    #transformer le dictionnaire en list
    list = dicLit(dic)

    #ajouter la clef a la liste "list"
    addclef(list, clef)

    #transformer les int de la liste en str et stocker dans une autre liste str "list1"
    list1 = intStr(list)

    #ajouter les 0 devant un nombre pour creer les paquet
    addpaq(list1)

    #separer les chiffre 2 par 2 et returne une list int
    list2 = separater(list1, paq)

    #transformer les chiffre regroupe 2 par 2 en lettre
    return chiffreLettre(list2)


print(Ecesar(txt, paq, clef ))
