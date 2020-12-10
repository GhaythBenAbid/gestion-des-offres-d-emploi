from tkinter import *
import sqlite3



def connexion():
    conn = sqlite3.connect("DataBaseProjet.db")
    return conn


def WindowSetup(root):
    master = Frame(root)
    master.grid_columnconfigure((0, 1, 2,3,4), weight=1)
    return master

def Message(text,x,y,master):
    Label(master , text = text).grid(row=x , column=y)
    

def CreationLabel(text,x,y,master):
    Label(master , text = text).grid(row=x , column=y)
    label = Entry(master)
    label.grid(row=x , column=y+1)
    return label

def CreationButton(text,x,y,method,master):
    label = Button(master, text=text, command=method)
    label.grid(row=x , column=y )
    return label
