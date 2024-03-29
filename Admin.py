from tkinter import *
from tkinter import messagebox 
import sqlite3
import Setup


class Admin:
    
    #Admin Panel (UI)
    def __init__(self,master , adminId):

        #Frame Setup
        self.master = master

        self.ParaAdmin = LabelFrame(text="Menu Admin" , pady=20 , padx=20)
        Label(self.ParaAdmin , text="Admin Panel" , font=('Arial', 16 , 'bold')).grid(row=0,column=1, pady=20)        
        self.adminId = adminId
        

        #buttons setup
        self.AjoutBtn = Setup.CreationButton("Ajouter une demande d'emploi",1,0,self.AjoutEmploi,self.ParaAdmin)
        self.modifyBtn = Setup.CreationButton("Modifier une demande d'emploi",1,1,self.ModifierEmploi,self.ParaAdmin)
        self.deleteBtn = Setup.CreationButton("Supprimer une demande d'emploi",1,2,self.SupprimerEmploi,self.ParaAdmin)
        
        #output in the screen
        self.ParaAdmin.pack()        
        self.MenuAdmin = Frame()


    #Ajout une offre (UI)

    def AjoutEmploi(self):
        
        #destroy the old frame
        self.MenuAdmin.destroy()
        
        #setup the Ajouter Emploi new frame
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

        #output
        self.MenuAdmin.pack()


    #Method du button Ajouter
        #Ajouter les donneés et envoyer a la base de donneés
    def Ajouter(self):

        #connxion to the DB
        conn = Setup.connexion()
        c = conn.cursor()
        val = (self.nomSociete.get(), self.adrSociete.get(), self.numSociete.get() , self.emailSociete.get(),self.adminId,self.diplome.get(),self.qualification.get(),self.experience.get(),self.description.get())

        #insert the values
        c.execute("insert into offre values(null,?,?,?,?,?,?,?,?,?)",val)
        conn.commit()


    #Modifier une offre (UI)

    def ModifierEmploi(self):

        #destroy the old frame
        self.MenuAdmin.destroy()
        self.MenuAdmin = LabelFrame(text="Modifier une offre d'emploi" , pady=20 , padx=20)

        #setup the Modifier Emploi new frame
        self.jobid = Setup.CreationLabel("Reference : ",1,0,self.MenuAdmin)
        self.Rechercheoffre = Button(self.MenuAdmin, text="Rechercher",command=lambda : self.AfficheRecherche("modifier",self.Modifier)).grid(row=2,column=0)
        
        #output
        self.MenuAdmin.pack()
    
    #Afficher les offres par Reference (UI)

    def AfficheRecherche(self,msg,method):
        if self.RechercheRequete():
            _nomSociete = self.RechercheRequete()[0]
            _adrSociete = self.RechercheRequete()[1]
            _numSociete = self.RechercheRequete()[2]
            _emailSociete = self.RechercheRequete()[3]
            _diplome = self.RechercheRequete()[4]
            _qualification = self.RechercheRequete()[5]
            _experience = self.RechercheRequete()[6]
            _description = self.RechercheRequete()[7]

            self.nomSociete = Setup.CreationLabel("Nom Societe :",3,0,self.MenuAdmin)
            self.nomSociete.insert(0,_nomSociete)

            self.adrSociete = Setup.CreationLabel("Adresse Societe :",4,0,self.MenuAdmin)
            self.adrSociete.insert(0,_adrSociete)
            
            self.numSociete = Setup.CreationLabel("Num Tel Societe :",5,0,self.MenuAdmin)
            self.numSociete.insert(0,_numSociete)
            
            self.emailSociete = Setup.CreationLabel("Email Societe :",6,0,self.MenuAdmin)
            self.emailSociete.insert(0,_emailSociete)

            self.diplome = Setup.CreationLabel("diplome :",7,0,self.MenuAdmin)
            self.diplome.insert(0,_diplome)
            
            self.qualification = Setup.CreationLabel("qualification :",8,0,self.MenuAdmin)
            self.qualification.insert(0,_qualification)
            
            self.experience = Setup.CreationLabel("experience :",9,0,self.MenuAdmin)
            self.experience.insert(0,_experience)
            
            self.description = Setup.CreationLabel("description :",10,0,self.MenuAdmin)
            self.description.insert(0,_description)

            self.Rechercheoffre = Setup.CreationButton(msg,11,0,method,self.MenuAdmin)
            

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
        c.execute("select nom_s,adr_s,numtel_s,email_s,diplome,qualification,experience,description from offre where jobid=?", val)
        recherche = c.fetchone()
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
        