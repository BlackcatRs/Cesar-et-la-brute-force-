#!/usr/bin/env python3

from OutilsCrypto import *

#txt="bonjour"
#clef=3
txt = input("Entrez votre texte ici : ")
paq = int(input("Entrez nobre de paquet : "))
clef = int(input("Entrez votre clef : "))

def Ecesar(txt, clef) :

    dic=paquet(txt, paq) #transformer le texte en chiffre par paquet de paq et stocker dans un dictionnaire

    #transformer le dictionnaire en list
    list = []
    for value in dic.values():
        list.append(value)
    print("votre texte <<", txt, ">> en chiffre", list,  "par paquet de", paq)

    #ajouter la clef a la liste
    compteur=0
    for value in list:
        list[compteur]+=clef
        compteur+=1

    #transformer les int de la liste en str et stocker dans une autre liste "liste1"
    list1 = []
    for value in list:
        list1.append(str(value))

    #ajouter les 0 devant un nombre pour creer les paquet
    compteur=0
    for value in list1:
        if len(value) < paq*2:
            list1[compteur]='0'+value
        compteur=+1
    print(list1)

    #separer les chiffre 2 par 2
    list2 = []
    for value in list1:
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
    print(list2)

    #transformer les chiffre regroupe 2 par 2 en lettre
    motcrypte = ''
    for element in list2:
        motcrypte+=xedoc(element)

    return motcrypte

print("Voila votre texte codee", Ecesar(txt,clef))
