# -*-coding:utf-8 -*
#Trier la liste d'objet eleve par ses attributs
def tri(liste):
    liste2=[]
    liste3=[]
    listeAttributClass=[]
    #on cree une liste qui contiendra toute les valeurs du minimum jusqu'au maximum
    for i in range(21):
        liste2.append(i)
        if i != 20:
            liste2.append(i + 0.5)

    #On compare chaque element de la liste2 a liste en partant du plus petit, si les deux element sont egaux on place l'objet dans la liste
    for i in range(len(liste2)):
        for j in range(len(liste)):
            if liste[j].moyenneGenerale==liste2[i]:
                liste3.append(liste[j])
    liste3.reverse()
    return liste3 #liste3 qui est la liste triee contenant les classe"""