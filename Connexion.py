import sqlite3

conn = sqlite3.connect("DataBaseProjet.db")
"""
c = conn.cursor()

c.execute("" CREATE TABLE admin(
    id_a integer,
    nom_a text,
    prenom_a text,
    email_a text,
    password_a text,
    Primary key(id_a)
)
"")

c.execute("insert into admin values(1,'Ghayth','Ben Abid','ghaythbenabid0@gmail.com','admin123')")

c.execute("" CREATE TABLE demandeur(
    id_d integer,
    nom_d text,
    prenom_d text,
    email_d text,
    password_d text,
    Primary key(id_d)
)
"")

c.execute("insert into demandeur values(1,'user15','test1','usertest18@gmail.com','user15')")

c.execute("" CREATE TABLE offre(
    jobID integer PRIMARY KEY AUTOINCREMENT,
    nom_s text,
    adr_s text,
    numtel_s text,
    email_s text,
    admin_id integer,
    FOREIGN KEY (admin_id) REFERENCES admin(id_a)
)
"")

conn.commit()


"""
c = conn.cursor()

c.execute(""" CREATE TABLE postuler(
    id_demendeur integer,
    id_offre integer,
    primary key(id_demendeur , id_offre)
)




""")



conn.commit()


conn.close()
