#!/usr/bin/env python3

from OutilsCrypto import *

txt="bonjourz"
clef=3


def Ecesar(txt, clef, paq=2) :
    list = [] #pour stocker les resultat a la fin
    var=paquet(txt, 1) #transformer le txt en dic

    list1=[]
    for valeur in var.values():
        list1.append(valeur)

    list2=[]
    b=0
    res=int((len(list1)-(len(list1)%paq))/paq)
    print(res)
    for values in range(res):
        i=0
        a=''
        while i < paq:
            a+=str(list1[b])
            i+=1 #comteur
            b+=1 #sauter lettre par lettre
        list2.append(a)
    print(list2)

    for valeur in list2:
        #print(valeur)
        trans = int(valeur)
        trans += clef #ajouter la cle
        trans %= mod2base(paq) #modulo 26
        print(trans)
        #separer les lettre 2 par deux puis les transformer en lettre
        list.append(xedoc(trans)) #ajoute les lettre converti des numero

    txtCodee = ""
    for value in list:
        txtCodee += value

    return txtCodee



print("Voila votre text <<", txt,">> codee par paquet de 1 : ", Ecesar(txt, clef))
print(paquet(txt, 1).values())

sds = [1, 17, 1, 42%26, 14, 23, 17, 28%26]

for value in sds:
    a=xedoc(value)
    print(a)
