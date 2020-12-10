from tkinter import *
import sqlite3
import LoginPage


if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x500")
    app = LoginPage.LoginPage(root)
    
    root.mainloop()   