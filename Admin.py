from tkinter import *
from tkinter import messagebox 
import sqlite3
import Setup


class Admin:
    
    #Admin Panel (UI)
    def __init__(self,master , adminId):
        self.master = master

        self.adminId = adminId

        
        
        self.ParaAdmin = LabelFrame(text="ParaAdmin" , pady=20 , padx=20)

        Label(self.ParaAdmin , text="Admin Panel" , font=('Arial', 16 , 'bold')).grid(row=0,column=1, pady=20)        
        
        self.AjoutBtn = Setup.CreationButton("Ajouter une demande d'emploi",1,0,self.AjoutEmploi,self.ParaAdmin)
        self.modifyBtn = Setup.CreationButton("Modifier une demande d'emploi",1,1,self.ModifierEmploi,self.ParaAdmin)
        self.deleteBtn = Setup.CreationButton("Supprimer une demande d'emploi",1,2,self.SupprimerEmploi,self.ParaAdmin)
        


        self.ParaAdmin.pack()
        
        self.MenuAdmin = Frame()


    #Ajout une offre (UI)

    def AjoutEmploi(self):
        
        
        self.MenuAdmin.destroy()
        
        self.MenuAdmin = LabelFrame(text="Ajouter une offre d'emploi" , pady=20 , padx=20)
        
        self.nomSociete = Setup.CreationLabel("Nom Societe :",1,0,self.MenuAdmin)
        self.adrSociete = Setup.CreationLabel("Adresse Societe :",2,0,self.MenuAdmin)
        self.numSociete = Setup.CreationLabel("Num Societe :",3,0,self.MenuAdmin)
        self.emailSociete = Setup.CreationLabel("Email Societe :",4,0,self.MenuAdmin)
        self.diplome = Setup.CreationLabel("Diplome :",5,0,self.MenuAdmin)
        self.qualification = Setup.CreationLabel("Qualification :",6,0,self.MenuAdmin)
        self.experience = Setup.CreationLabel("Experience :",7,0,self.MenuAdmin)
        self.description = Setup.CreationLabel("Description :",8,0,self.MenuAdmin)
        self.ajouteroffre = Setup.CreationButton("Ajouter cette offre",9,0,self.Ajouter,self.MenuAdmin)

        self.MenuAdmin.pack()

    #Method du button Ajouter
        #Ajouter les donneés et envoyer a la base de donneés

    def Ajouter(self):
        conn = Setup.connexion()
        c = conn.cursor()
        val = (self.nomSociete.get(), self.adrSociete.get(), self.numSociete.get() , self.emailSociete.get(),self.adminId,self.diplome.get(),self.qualification.get(),self.experience.get(),self.description.get())
        c.execute("insert into offre values(null,?,?,?,?,?,?,?,?,?)",val)
        conn.commit()


    #Modifier une offre (UI)

    def ModifierEmploi(self):

        self.MenuAdmin.destroy()
        self.MenuAdmin = LabelFrame(text="Modifier une offre d'emploi" , pady=20 , padx=20)


        self.jobid = Setup.CreationLabel("Reference : ",1,0,self.MenuAdmin)
        self.Rechercheoffre = Button(self.MenuAdmin, text="Rechercher",command=lambda : self.AfficheRecherche("modifier",self.Modifier)).grid(row=2,column=0)
        

        self.MenuAdmin.pack()
    
    #Afficher les offres par Reference (UI)

    def AfficheRecherche(self,msg,method):
        if self.RechercheRequete():
            _nomSociete = self.RechercheRequete()[0]
            _adrSociete = self.RechercheRequete()[1]
            _numSociete = self.RechercheRequete()[2]
            _emailSociete = self.RechercheRequete()[3]

            self.nomSociete = Setup.CreationLabel("Nom Societe :",3,0,self.MenuAdmin)
            self.nomSociete.insert(0,_nomSociete)

            self.adrSociete = Setup.CreationLabel("Adresse Societe :",4,0,self.MenuAdmin)
            self.adrSociete.insert(0,_adrSociete)
            
            self.numSociete = Setup.CreationLabel("Num Tel Societe :",5,0,self.MenuAdmin)
            self.numSociete.insert(0,_numSociete)
            
            self.emailSociete = Setup.CreationLabel("Email Societe :",6,0,self.MenuAdmin)
            self.emailSociete.insert(0,_emailSociete)

            self.Rechercheoffre = Setup.CreationButton(msg,7,0,method,self.MenuAdmin)
            
        else:
            self.MessageErreur = Setup.Message("id non trouvé",3,0,self.MenuAdmin)


    #Method du button Modifier
        #Modifier les donneés et envoyer a la base de donneés
    def Modifier(self):
        conn = Setup.connexion()
        c = conn.cursor()
        sql = "Update offre set nom_s = ? ,adr_s = ? ,numtel_s = ?,email_s = ?,admin_id = 1 where jobID=?"
        val = (self.nomSociete.get(), self.adrSociete.get(), self.numSociete.get(),self.emailSociete.get(),self.jobid.get())
        c.execute(sql,val)
        conn.commit()
        messagebox.showinfo("tk", "Modification effectué avec success") 



    #Method Recherche
        #Rechercher dans la base et retourne (nom Societe , Adresse Societe , Num Tel Societe , Email Societe ...)

    def RechercheRequete(self):
        conn = Setup.connexion()
        c = conn.cursor()
        val = (self.jobid.get(),)
        c.execute("select nom_s,adr_s,numtel_s,email_s,admin_id from offre where jobid=?", val)
        recherche = c.fetchone()
        return recherche
    
    
    def RechercheTout(self):
        conn = Setup.connexion()
        c = conn.cursor()
        c.execute("select * from offre")
        recherche = c.fetchall()
        return recherche

    



    def SupprimerEmploi(self):
        self.MenuAdmin.destroy()
        self.MenuAdmin = LabelFrame(text="Supprimer une offre d'emploi" , pady=20 , padx=20)

        self.jobid = Setup.CreationLabel("Reference : ",1,0,self.MenuAdmin)
        self.Rechercheoffre = Button(self.MenuAdmin, text="Rechercher",command=lambda : self.AfficheRecherche("Supprimer",self.Supprimer)).grid(row=2,column=0)
        self.MenuAdmin.pack()

    def Supprimer(self):
        conn = Setup.connexion()
        c = conn.cursor()
        sql = "delete from offre where jobID=?"
        val = (self.jobid.get() ,)
        c.execute(sql,val)
        conn.commit()
        messagebox.showinfo("tk", "suppression effectué avec success") 
        