import time 
import math
import random


#####################################################
#		   	 	A FAIRE POUR LE TP CESAR			#
#####################################################

#codex(B)=1
#Code erreur : -1
def codex(c) :
    try :
        c=str(c)
        c=c[0].upper()
    except : return -1
    n=ord(c)-ord('A')
    if(n>25 or n<0) : return -1
    return n

#xedoc(1)=B
#Code erreur : '?'
def xedoc(n) :
    try : n=int(n)
    except : return '?'
    if(n>25 or n<0) : return '?'
    return chr(n+ord('A'))

#paquet("ABCD", 2)={0:1, 1:203}
#Code erreur : dico vide
def paquet(txt, paq=1) :
    try :
        txt=str(txt)
        paq=int(paq)
    except : return dict()
    if(paq<0) : return dict()

    res=dict()
    n=len(txt)
    i=0
    nb_paq=-1
    while(i<n) :
        if(i%paq==0) :
            nb_paq+=1
            res[nb_paq]=0
        x=codex(txt[i])
        if(x==-1) : return {}
        res[nb_paq]=res[nb_paq]*100+x
        i+=1

    while(i%paq!=0) : 
        res[nb_paq]*=100
        i+=1
    return res

#mod2base(2)=2526
#Code erreur : 26
def mod2base(paq=1) :
    try : paq=int(paq)
    except : return mod2base()
    res=0
    i=0
    while(i<paq) :
        res=100*res+25
        i+=1
    return res+1

#Gestion des caractère accentué
def Filtre(txt) :
    res=""
    for c in txt.lower() :
        if(ord('a')<=ord(c)<=ord('z')) : res+=c
        if(c=='à' or c=='â' or c=='ä' or c=='á' or c=='å') : res+='a'
        elif(c=='ç') : res+='c'
        elif(c=='é' or c=='è' or c=='ê' or c=='ë') : res+='e'
        elif(c=='ï' or c=='î' or c=='ì' or c=='í') : res+='i'
        elif(c=='ö' or c=='ò' or c=='ô' or c=='ø' or c=='ó') : res+='o'
        elif(c=='û' or c=='ü' or c=='ù' or c=='ú') : res+='u'
        elif(c=='æ') : res+='ae'
        elif(c=='œ') : res+='oe'
        elif(c=='ÿ') : res+='y'
        elif(c=='ñ') : res+='n'
        elif(c=='ß') : res+='ss'
    return res


#Création d'un arbre représentant le dictionnaire
#En paramètre la langue FR, ANG
def MonDico(lang="FR") :
    try : lang=str(lang)
    except : lang="FR"

    Racine=dict()

    def constructBranche(mot):
        Arbre = Racine;
        for c in mot:
            #Si le cara c n'existe pas on le crée (permet en plus de gérer les répétitions éventuelles)
            if not (c in Arbre): 
                Arbre[c] = dict()
                Arbre[c]['FINMOT']=False
            #On avance dans l'arbre
            Arbre = Arbre[c]
        #Arrivé à la fin on marque que le mot est fini
        Arbre["FINMOT"] = True

    if(lang in {"ANG", "ALL", "ESP", "IT", "DAN", "NOR", "SWI", "NED"}) : dico = "Dictionnaires/Dictionnaire"+lang+".txt"
    else : dico = "Dictionnaires/DictionnaireFR.txt"

    with open(dico, "r", encoding='utf8') as f :
        for ligne in f.readlines() : 
            constructBranche(Filtre(ligne.strip()).upper())
    return Racine

#Calcul la pertinance d'une phrase avec l'arbre
def pertinence(phrase, arbre) :
    pert=0
    n=len(phrase)
    i=0
    while(i<n) :
        test=True
        j=i
        positionDico=arbre
        while(j<n) :
            cara=phrase[j]
            try : x=positionDico[cara]
            except : break
            if(x['FINMOT']) : pert+=1
            positionDico=x
            j+=1
        i+=1
    return pert
