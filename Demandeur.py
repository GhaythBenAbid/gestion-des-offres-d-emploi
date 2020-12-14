from tkinter import *
import sqlite3
import Setup

class Demandeur():

    def __init__(self , master , demandeurID):
        
        #Frame Setup
        self.master = master

        self.ParaDemandeur = LabelFrame(text="Menu Demandeur", pady=20 , padx=20)
        Label(self.ParaDemandeur , text="Demandeur Panel" , font=('Arial', 16 , 'bold')).grid(row=0,column=1, pady=20)        
        self.demandeurID = demandeurID

        self.afficherlesoffres = Setup.CreationButton("Afficher les offres d'emploi",1,1,self.AfficherTousLesOffres,self.ParaDemandeur)
        self.AjouterDemande = Setup.CreationButton("Ajouter Votre Demande",2,1,self.AjouterVotreDemande,self.ParaDemandeur)

        self.ParaDemandeur.pack()
        self.MenuDemendeur = Frame()

        


    def AfficherTousLesOffres(self):

        self.MenuDemendeur.destroy()
        self.MenuDemendeur = LabelFrame(text="Afficher" , pady=20 , padx=20)


        conn = Setup.connexion()
        c = conn.cursor()
        sql = "select * from offre"
        c.execute(sql)
        recherche = c.fetchall()

        Label(self.MenuDemendeur , text="job_id" , font=('bold')   ).grid(row=0 , column=0)
        Label(self.MenuDemendeur , text="nomSociete" , font=('bold')).grid(row=0 , column=1)
        Label(self.MenuDemendeur , text="adrSociete" , font=('bold')).grid(row=0 , column=2)
        Label(self.MenuDemendeur , text="numSociete" , font=('bold')).grid(row=0 , column=3)
        Label(self.MenuDemendeur , text="emailSociete" , font=('bold')).grid(row=0 , column=4)
        Label(self.MenuDemendeur , text="diplome" , font=('bold')).grid(row=0 , column=5)
        Label(self.MenuDemendeur , text="qualification" , font=('bold')).grid(row=0 , column=6)
        Label(self.MenuDemendeur , text="experience" , font=('bold')).grid(row=0 , column=7)
        Label(self.MenuDemendeur , text="description" , font=('bold')).grid(row=0 , column=8)

        
        ligne = 1
        offreId = []
        for rech in recherche:
            _job_id = rech[0]
            _nomSociete = rech[1]
            _adrSociete = rech[2]
            _numSociete = rech[3]
            _emailSociete = rech[4]
            _diplome = rech[6]
            _qualification = rech[7]
            _experience = rech[8]
            _description = rech[9]
            

            Label(self.MenuDemendeur , text=_job_id ).grid(row=ligne , column=0)
            Label(self.MenuDemendeur , text=_nomSociete).grid(row=ligne , column=1)
            Label(self.MenuDemendeur , text=_adrSociete).grid(row=ligne , column=2)
            Label(self.MenuDemendeur , text=_numSociete).grid(row=ligne , column=3)
            Label(self.MenuDemendeur , text=_emailSociete).grid(row=ligne , column=4)
            Label(self.MenuDemendeur , text=_diplome).grid(row=ligne , column=5)
            Label(self.MenuDemendeur , text=_qualification).grid(row=ligne , column=6)
            Label(self.MenuDemendeur , text=_experience).grid(row=ligne , column=7)
            Label(self.MenuDemendeur , text=_description).grid(row=ligne , column=8)
            
            ligne+=1

        self.MenuDemendeur.pack()

        
    def AjouterVotreDemande(self):
        self.MenuDemendeur.destroy()
        self.MenuDemendeur = LabelFrame(text="Ajouter" , pady=20 , padx=20)

        self.jobID = Setup.CreationLabel("offre ID",0,0,self.MenuDemendeur)
        self.CIN = Setup.CreationLabel("CIN",1,0,self.MenuDemendeur)
        self.Nom = Setup.CreationLabel("Nom",2,0,self.MenuDemendeur)
        self.adresse = Setup.CreationLabel("adresse",3,0,self.MenuDemendeur)
        self.numTel = Setup.CreationLabel("numero Telephone",4,0,self.MenuDemendeur)
        self.Education = Setup.CreationLabel("education",5,0,self.MenuDemendeur)
        self.experience = Setup.CreationLabel("experience",6,0,self.MenuDemendeur)
        self.ajouter = Setup.CreationButton("ajouter",7,0,self.Ajouter,self.MenuDemendeur)

        self.MenuDemendeur.pack()

    def Ajouter(self):
        conn = Setup.connexion()
        c = conn.cursor()
        val = (self.demandeurID  , self.jobID.get() , self.CIN.get() , self.Nom.get() , self.adresse.get() , self.numTel.get() , self.Education.get() , self.experience.get() , )
        c.execute("insert into postuler values(?,?,?,?,?,?,?,?)" , val)
        conn.commit()
        

        
