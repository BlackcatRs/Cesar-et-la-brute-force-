#!/usr/bin/env python3

from OutilsCrypto import *

#transformer les chiffre regroupe 2 par 2 en lettre
def chiffreLettre(listInt):
    motcrypte = ''
    for element in listInt:
        motcrypte+=xedoc(element%26)
    return motcrypte

def decrypt(listInt, clef):
    listDecypte=[]
    for value in listInt:
        listDecypte.append((value-clef)%2526)
    return listDecypte


def intStr(intList):
    list1 = []
    for value in intList:
        list1.append(str(value))
    return list1

def addpaq(strlist, paq):
    compteur=0
    for value in strlist:
        if len(value) < paq*2:
            a=paq*2-len(value)
            strlist[compteur]=(a*'0')+value
        compteur+=1

#separer les chiffre 2 par 2 et retourne une liste int
def separaterStr(strList):
    list = []
    for value in strList:
        modulo=len(value)%2
        i=0

        if modulo == 1:
            a=value[i]
            list.append(int(a))
            i+=1

        e=int((len(value)-modulo)/2)

        #a modifier
        for z in range(e):
            a=''
            x=0
            while x < 2:
                a+=value[i]
                i+=1
                x+=1
            list.append(int(a))


    return list



#message crypte
#list=[2138, 523, 1651, 1650, 712, 1434, 1834, 2338, 412, 721, 212, 708]
list=[114, 1309, 1420, 1700]
#strlist = ['117', '1312', '1423', '1703']
intlist = [2138, 523, 1651, 1650, 712, 1434, 1834, 2338, 412, 721, 212, 708]

for number in range(2526):
    a= decrypt(intlist, number)
    b= intStr(a)
    c= separaterStr(b)
    d= chiffreLettre(c)
    print(d)
