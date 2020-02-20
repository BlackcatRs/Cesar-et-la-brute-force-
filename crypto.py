#!/usr/bin/env python3

from OutilsCrypto import *

txt="bonjour"
clef=3

'''
def Ecesar(txt, clef, paq=1) :
    list = []
    var=paquet(txt, 1) #transformer le txt en dic
    for valeur in var.values():
        valeur += clef #ajouter la cle
        valeur %= mod2base(paq) #modulo 26
        list.append(xedoc(valeur)) #ajoute les lettre converti des numero

    txtCodee = ""
    for value in list:
        txtCodee += value

    return txtCodee



print("Voila votre text <<", txt,">> codee par paquet de 1 : ", Ecesar(txt, clef))

'''


list=[1, 2, 5, 6, 7, 1]
list1=[]
paq = 3

'''#1er 2 chiffre
b=0
i=0
a=''

while i < paq:
    a+=str(list[b])
    i+=1
    b+=1

list1.append(a)

 #2eme 2 chifrre
i=0
c=''
while i < paq:
    c+=str(list[b])
    i+=1
    b+=1

list1.append(c)

'''
b=0
for values in range(paq):
    i=0
    a=''
    while i < paq:
        a+=str(list[b])
        i+=1
        b+=1
    list1.append(a)

print(list1)
