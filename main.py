# -*-coding:utf-8 -*
import os
from classe import *
from fonction import *
from pickle import *
from tkinter import *
from tkinter.tix import *


listeEleve=[]

#Bouton valider qui enregistre touts les informations sur l'eleve
def valider():
    nom=nomEntry.get()
    nomEntry.delete(0,len(nom))
    prenom=prenomEntry.get()
    prenomEntry.delete(0, len(prenom))
    moyenne1=note1Entry.get()
    note1Entry.delete(0, len(moyenne1))
    moyenne2=note2Entry.get()
    note2Entry.delete(0, len(moyenne2))
    if (nom == "" or " " in nom) or (prenom == "" or " " in prenom) or ((not moyenne1.isnumeric()) or (moyenne1 == "" or " "  in moyenne1) or (int(moyenne1)<0 and int(moyenne1)>20)) or ((not moyenne2.isnumeric()) or (moyenne2 == "" or " " in moyenne2) or  (int(moyenne2)<0 and int(moyenne2)>20)):
        confirmationLabel['text'] = ""
        confirmationLabel['fg'] = 'red'
        confirmationLabel['text'] += "Elève non enregistré, verifier\nbien que le nom et le prenom\nne soit pas vide ou ne contienne\npas d'espace et que les moyennes\nsoient valide(entre 0 et 20) "
    else:
        moyenne1, moyenne2 = int(moyenne1), int(moyenne2)
        confirmationLabel['text'] = ""
        confirmationLabel['fg'] = 'black'
        confirmationLabel['text'] += "L'éleve " + nom + "\n" + prenom + " a bien\nété enregistré "
        e1 = Eleve(nom, prenom, moyenne1, moyenne2)
        listeEleve.append(e1)
        e1.calculMoy()

#Deuxieme fenetre bulletin
def fenetreBuletin():

    fenetre2=Tk()

    #fenetre principal
    fenetre2.title("My app")
    fenetre2.geometry("720x675")
    fenetre2.minsize(700,675)
    fenetre2.maxsize(700,675)
    fenetre2.iconbitmap("icon.ico")
    fenetre2.config(background='#a99bff')

    listeTriee=tri(listeEleve)
    #frame contenant la liste des etudiant
    frameListe = Frame(fenetre2, bg='#a99bff', relief=SUNKEN)
    for i in range(len(listeEleve)):
        labelListe = Label(frameListe,text=str(i+1)+"e "+listeTriee[i].getNom()+" "+listeTriee[i].getPrenom()+" ; Moyenne generale: "+str(listeTriee[i].moyenneGenerale)+" ; "+listeTriee[i].mention(),bg='#a99bff',font=('Eras Demi ITC',10))
        labelListe.grid(row=i,column=0)
    frameListe.pack()

    fenetre2.mainloop()

#Bouton changer de page
def bulletin():
    fenetreBuletin()

#Enregistrer la liste d'eleve
def enregistrer():
    listeTriee = tri(listeEleve)
    with open("listeEleve","wb") as fic:
        picleo=Pickler(fic)
        picleo.dump(listeTriee)

#charger la liste precedente
def charger():
    global listeEleve
    try:
        with open("listeEleve","rb") as fic:
            picleo=Unpickler(fic)
            listeEleve=picleo.load()
    except FileNotFoundError:
        confirmationLabel['text'] = ""
        confirmationLabel['fg'] = 'red'
        confirmationLabel['text'] += "Acune liste a charger"

#bouton imprimer dans un fichier texte le buletin
def imprimer():
    global listeEleve
    if listeEleve!=[]:
        listeTriee=tri(listeEleve)
        chaine = ""
        for i in range(len(listeTriee)):
            chaine+=str(i+1)+"e "+listeTriee[i].getNom()+" "+listeTriee[i].getPrenom()+" ; Moyenne generale: "+str(listeTriee[i].moyenneGenerale)+" ; "+listeTriee[i].mention()+"\n"
        with open("Bulletin.docx","w") as fic2:
            fic2.write(chaine)
    else:
        confirmationLabel['text'] = ""
        confirmationLabel['fg'] = 'red'
        confirmationLabel['text'] += "Acune liste a imprimer"

#Bouton pour quitter
def quitter():
    fenetrePrincipal.destroy()

#Definition du cadre et surface de l'interface
fenetrePrincipal=Tk()
bulle=Balloon(fenetrePrincipal)

fenetrePrincipal.title("Fandr's app")
fenetrePrincipal.geometry("720x400")
fenetrePrincipal.minsize(720,400)
fenetrePrincipal.maxsize(720,400)
fenetrePrincipal.iconbitmap("icon.ico")
fenetrePrincipal.config(background='#a99bff')

#image de fond
canvaImage = Canvas(fenetrePrincipal,width=400,height=500,bg='#a99bff',bd=0,highlightthickness=0)
imageFond = PhotoImage(file="student.png").zoom(35).subsample(35)
canvaImage.create_image(200,250,image=imageFond)
canvaImage.place(x=400,y=0)

#Titre
frameTitre = Frame(fenetrePrincipal,bg='#a99bff',relief=SUNKEN,bd=0,highlightthickness=0)
titre = Label(frameTitre,text="Gestion élève",font=("Arial Black",20),bg='#a99bff')
titre.pack()
frameTitre.pack()

#Bloc des barres de texte(intput) pour entrer les infomation
frameInformation = Frame(fenetrePrincipal,bg='#a99bff',relief=SUNKEN)
nomLabel = Label(frameInformation,text="Nom: ",bg='#a99bff',font=('Eras Demi ITC',10))
nomEntry = Entry(frameInformation)
prenomLabel = Label(frameInformation,text="Prenom: ",bg='#a99bff',font=('Eras Demi ITC',10))
prenomEntry = Entry(frameInformation)
note1Label = Label(frameInformation,text="Moyenne \n1er semestre: ",bg='#a99bff',font=('Eras Demi ITC',10))
note1Entry = Entry(frameInformation)
note2Label = Label(frameInformation,text="Moyenne \n2eme semestre: ",bg='#a99bff',font=('Eras Demi ITC',10))
note2Entry = Entry(frameInformation)
boutonEnregistrer = Button(frameInformation,text="Valider",command=valider,bg='#dbdcff',font=('Arial Black',8))
confirmationLabel = Label(frameInformation, text="", bg='#a99bff')

#positionnement des elements
frameInformation.place(x=0,y=75)
nomLabel.grid(row=0,column=0)
nomEntry.grid(row=0,column=1)
prenomLabel.grid(row=1,column=0)
prenomEntry.grid(row=1,column=1)
note1Label.grid(row=2,column=0)
note1Entry.grid(row=2,column=1)
note2Label.grid(row=3,column=0)
note2Entry.grid(row=3,column=1)
boutonEnregistrer.grid(row=4,column=1)
confirmationLabel.grid(row=5,column=1)

#Bloc bouton
frameBouton = Frame(fenetrePrincipal,bg='#a99bff',relief=SUNKEN)
boutonBulletin=Button(frameBouton,text="Produire bulletin",command=bulletin,bg='#dbdcff',font=('Arial Black',8))
boutonEnregistrer=Button(frameBouton,text="Enregistrer liste",command=enregistrer,bg='#dbdcff',font=('Arial Black',8))
boutonCharger=Button(frameBouton,text="Charger liste",command=charger,bg='#dbdcff',font=('Arial Black',8))
boutonImprimer=Button(frameBouton,text="Imprimer bulletin",command=imprimer,bg='#dbdcff',font=('Arial Black',8))

#Creation des bulles pour les buttons
bulle.bind_widget(boutonBulletin,balloonmsg="Produire bulletin dans une seconde fenêtre ")
bulle.bind_widget(boutonEnregistrer,balloonmsg="Enregistrer (ou écraser la sauvegare précédent)\nla liste d'élève que vous avez entré")
bulle.bind_widget(boutonCharger,balloonmsg="Charger la liste d'élève enregistré précédemment")
bulle.bind_widget(boutonImprimer,balloonmsg="Mettre le bulletin dans un fichier word")

#placement des boutons
boutonBulletin.grid(row=0,column=0)
boutonEnregistrer.grid(row=1,column=0)
boutonCharger.grid(row=2,column=0)
boutonImprimer.grid(row=3,column=0)
frameBouton.place(x=2.5,y=275)

#bouton quitter
boutonQuit=Button(fenetrePrincipal,text="Quitter",command=quitter,bg='#dbdcff',font=('Arial Black',8))
boutonQuit.place(x=650,y=350)

copyRight = Label(fenetrePrincipal,text="©CopyRight RAVELOHARISON Fandresena",bg='#a99bff')
copyRight.place(x=0,y=380)

fenetrePrincipal.mainloop()
os.system("pause")