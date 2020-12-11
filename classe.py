# -*-coding:utf-8 -*
class Eleve:
    compteur=0

    #constructeur
    def __init__(self,nom,prenom,moyenne1,moyenne2):
        Eleve.compteur+=1
        self.nom=nom
        self.prenom=prenom
        self.moyenne1=moyenne1
        self.moyenne2=moyenne2
        self.moyenneGenerale=0

    #proprietes,accesseurs et mutateur
    def getNom(self):
        return self.nom
    def setNom(self,gnom):
        self.nom=gnom
    def getPrenom(self):
        return self.prenom
    def setPrenom(self,gprenom):
        self.nom=gprenom
    def getMoyenne1(self):
        return self.moyenne1
    def setMoyenne1(self,gmoyenne1):
        self.nom=gmoyenne1
    def getMoyenne2(self):
        return self.moyenne2
    def setMoyenne2(self,gmoyenne2):
        self.nom=gmoyenne2

    #Calcul de la moyenne generale
    def calculMoy(self):
        self.moyenneGenerale=(self.moyenne1+self.moyenne2)/2
    
    #definotion de la mention par rapport a la moyenne generale
    def mention(self):
        if self.moyenneGenerale<10:
            return "Redoublant, insuffisant"
        elif self.moyenneGenerale>9 and self.moyenneGenerale<13:
            return "Passant, mention passable"
        elif self.moyenneGenerale>12 and self.moyenneGenerale<18:
            return "Passant, mention bien"
        elif self.moyenneGenerale>17 and self.moyenneGenerale<=20:
            return "Passant, mention tres bien"
        else:
            return "Moyenne non valide"