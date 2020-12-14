from tkinter import *
from tkinter import ttk
import sqlite3
import Admin
import Demandeur
import Setup

class LoginPage:
    def __init__(self, master):
        
        #Frame Setup
        self.master = master
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.frame = Frame(self.master)

        #Entrys and labels setup
        self.myLabel1 = Label(self.frame, text='USERNAME')
        self.UserIn = Entry(self.frame)
        self.myLabel2 = Label(self.frame, text='PASSWORD')
        self.PassIn = Entry(self.frame)
        self.btn = Button(self.frame, text="Log in" , command=self.LogIn)
        
        #positioning the labels and the entrys
        self.myLabel1.grid(row=1,column=1)
        self.UserIn.grid(row=2,column=1)
        self.myLabel2.grid(row=3,column=1)
        self.PassIn.grid(row=4,column=1)
        self.btn.grid(row=5,column=1)

        #print out the UI
        self.frame.pack()


    def LogIn(self):

        #Setup the connection and cursor
        conn = Setup.connexion()
        c = conn.cursor()

        #call out the username and password inputs
        u = self.UserIn.get()
        p = self.PassIn.get()

        #init the exec
        val = (u, p,)
        
        #exectue the query from admin table
        c.execute("select id_a from admin where email_a=? and password_a=?", val)
        logAdmin = c.fetchone()

        #exectue the query from demendeur table
        c.execute("select count(*) from demandeur where email_d=? and password_d=?", val)
        logDemandeur = c.fetchone()
        
        #check if which user has entred his informations
        if (logAdmin is not None):
            self.frame.destroy()
            admin = Frame(self.master)
            Admin.Admin(admin , logAdmin)

        elif(logDemandeur is not None):
            self.frame.destroy()
            demandeur = Frame(self.master)
            Demandeur.Demandeur(demandeur , logDemandeur)
            
