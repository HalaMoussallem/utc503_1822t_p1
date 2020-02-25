from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from note import *
import sqlite3
from functools import reduce

def raise_frame(Frame):
    Frame.tkraise()

db=sqlite3.connect("newdb.db")
db.row_factory=sqlite3.Row
db.execute("create table if not exists Etudiant(id integer primary key autoincrement,nom txt, prenom txt,niveau txt)")
db.execute("create table if not exists Cours(code txt ,intitule txt, niveau txt)")
db.execute("create table if not exists Note(code txt ,ide integer, note integer)")
db.commit()

root=Tk()
root.title("Projet")

Home=Frame(root)
Etudiant=Frame(root)
Note=Frame(root)
Cours=Frame(root)
AjouterEtudiant=Frame(root)
AjouterCours=Frame(root)
AjouterNote=Frame(root)
SupprimerEtudiant=Frame(root)
SupprimerCours=Frame(root)
SupprimerNote=Frame(root)
CalculerNoteEtudiant=Frame(root)
ConsulterNoteEtudiant=Frame(root)
CalculerNoteClasse=Frame(root)
ConsulterNoteClasse=Frame(root)
EditerNote=Frame(root)
EditerEtudiant=Frame(root)
EditerCours=Frame(root)
EditerNote1=Frame(root)
EditerEtudiant1=Frame(root)
EditerCours1=Frame(root)

Home.grid(row=0,column=0,sticky='news')
Etudiant.grid(row=0,column=0,sticky='news')
Cours.grid(row=0,column=0,sticky='news')
Note.grid(row=0,column=0,sticky='news')
AjouterEtudiant.grid(row=0,column=0,sticky='news')
AjouterCours.grid(row=0,column=0,sticky='news')
AjouterNote.grid(row=0,column=0,sticky='news')
SupprimerEtudiant.grid(row=0,column=0,sticky='news')
SupprimerCours.grid(row=0,column=0,sticky='news')
SupprimerNote.grid(row=0,column=0,sticky='news')
CalculerNoteEtudiant.grid(row=0,column=0,sticky='news')
ConsulterNoteEtudiant.grid(row=0,column=0,sticky='news')
CalculerNoteClasse.grid(row=0,column=0,sticky='news')
ConsulterNoteClasse.grid(row=0,column=0,sticky='news')
EditerCours.grid(row=0,column=0,sticky='news')
EditerNote.grid(row=0,column=0,sticky='news')
EditerEtudiant.grid(row=0,column=0,sticky='news')
EditerCours1.grid(row=0,column=0,sticky='news')
EditerNote1.grid(row=0,column=0,sticky='news')
EditerEtudiant1.grid(row=0,column=0,sticky='news')


#dans frame home

b1=ttk.Button(Home,text="Etudiant")
b1.grid(row=0,column=0,ipadx=20,ipady=10,padx=20,pady=10,columnspa=2)

def b1Click():
    raise_frame(Etudiant)
b1.config(command=b1Click)

b2=ttk.Button(Home,text="Note")
b2.grid(row=1,column=2,ipadx=20,ipady=10,padx=20,pady=5,columnspa=2)

def b2Click():
    raise_frame(Note)
b2.config(command=b2Click)

b3=ttk.Button(Home,text="Cours")
b3.grid(row=2,column=4,ipadx=20,ipady=10,padx=20,pady=5,columnspa=2)

def b3Click():
    raise_frame(Cours)
b3.config(command=b3Click)

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

        
#dans frame etudiant
b=ttk.Button(Etudiant,text="<-- Back")
b.grid(row=5,column=0)
def backClick():
    raise_frame(Home)
b.config(command=backClick)

b1e=ttk.Button(Etudiant,text="Ajouter étudiant")
b1e.grid(row=0,column=0,ipadx=10,ipady=10,padx=20,pady=20)
def b1eClick():
    raise_frame(AjouterEtudiant)
b1e.config(command=b1eClick)


b2e=ttk.Button(Etudiant,text="Supprimer étudiant")
b2e.grid(row=0,column=1,ipadx=10,ipady=10,padx=20,pady=20)
def b2eClick():
    raise_frame(SupprimerEtudiant)
b2e.config(command=b2eClick)

b3e=ttk.Button(Etudiant,text="Editer étudiant")
b3e.grid(row=0,column=2,ipadx=10,ipady=10,padx=20,pady=20)
def b3eClick():
    raise_frame(EditerEtudiant1)    
b3e.config(command=b3eClick)

b4e=ttk.Button(Etudiant,text="Calculer la moyenne \n      d’un étudiant")
b4e.grid(row=3,column=0,ipadx=10,ipady=10,padx=20,pady=20,columnspa=2)
def b4eClick():
    raise_frame(CalculerNoteEtudiant)
b4e.config(command=b4eClick)

b5e=ttk.Button(Etudiant,text="Consulter les notes \n      d’un étudiant")
b5e.grid(row=3,column=1,ipadx=10,ipady=10,padx=20,pady=20,columnspa=2)
def b5eClick():
    raise_frame(ConsulterNoteEtudiant)
b5e.config(command=b5eClick)

#dans frame Ajouteretudiant
be=ttk.Button(AjouterEtudiant,text="<-- Back")
be.grid(row=5,column=0,pady=10,padx=10)
def backe():
    raise_frame(Etudiant)
be.config(command=backe)

bes=ttk.Button(AjouterEtudiant,text="Sauvegarder")
bes.grid(row=5,column=4,pady=10,padx=10)
def SaveEs():
    nom=e1.get()
    prenom=e2.get()
    niveau=Span.get()
    print(niveau)
    db.execute("insert into Etudiant(nom,prenom,niveau) values(?,?,?)",(nom,prenom,niveau))
    db.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    print("ajouter")


bes.config(command=SaveEs)

l1=ttk.Label(AjouterEtudiant,text="Nom:")
l1.grid(row=0,column=0,pady=10)
e1=ttk.Entry(AjouterEtudiant,width=40)
e1.grid(row=0,column=1,columnspa=3,pady=10)
l2=ttk.Label(AjouterEtudiant,text="Prenom:")
l2.grid(row=1,column=0,pady=10)
e2=ttk.Entry(AjouterEtudiant,width=40)
e2.grid(row=1,column=1,columnspa=3,pady=10)
l3=ttk.Label(AjouterEtudiant,text="Niveau:")
l3.grid(row=2,column=0,pady=10)
Span=StringVar()
e3=ttk.Radiobutton(AjouterEtudiant,text="A",variable=Span,value="A")
e3.grid(row=2,column=1)
e4=ttk.Radiobutton(AjouterEtudiant,text="B",variable=Span,value="B")
e4.grid(row=2,column=2)
e5=ttk.Radiobutton(AjouterEtudiant,text="C",variable=Span,value="C")
e5.grid(row=2,column=3)

#dans frame EditerEtudiant1

et=ttk.Button(EditerEtudiant1,text="<-- Back")
et.grid(row=5,column=0,pady=10,padx=10)
def etf():
    raise_frame(Etudiant)
et.config(command=etf)

l1sep=ttk.Label(EditerEtudiant1,text="ID etudiant:")
l1sep.grid(row=0,column=0,pady=10)
e1tbh=ttk.Entry(EditerEtudiant1,width=40)
e1tbh.grid(row=0,column=1,pady=10)


bconf=ttk.Button(EditerEtudiant1,text="editer")
bconf.grid(row=5,column=3,pady=10,padx=10)    
def etff():
    pop=e1tbh.get()
    sbh=db.execute("Select * from Etudiant where id={}".format(pop))
    rowbh=sbh.fetchone()
    if(rowbh):
        raise_frame(EditerEtudiant)
        e1t.insert(0,rowbh['nom'])
        e2t.insert(0,rowbh['prenom'])
        e3t.insert(0,rowbh['niveau'])
        
    else:
        messagebox.showinfo(title="error", message="Etudiant n'existe pas")
bconf.config(command=etff)    


#dans frame EditerEtudiant
bet=ttk.Button(EditerEtudiant,text="<-- Back")
bet.grid(row=5,column=0,pady=10,padx=10)
def backet():
    raise_frame(EditerEtudiant1)
    e1t.delete(0,END)
    e2t.delete(0,END)
    e3t.delete(0,END)
bet.config(command=backet)

best=ttk.Button(EditerEtudiant,text="Sauvegarder")
best.grid(row=5,column=3,pady=10,padx=10)
def SaveEst():
    pop=e1tbh.get()
    s1=e1t.get()
    s2=e2t.get()
    s3=e3t.get()

    db.execute("UPDATE Etudiant SET nom=(?), prenom=(?), niveau=(?) WHERE id=(?) ",(s1, s2, s3, pop))
    db.commit()
    messagebox.showinfo(title="error", message="Etudiant edité")
    e1t.delete(0,END)
    e2t.delete(0,END)
    e3t.delete(0,END)
    raise_frame(EditerEtudiant1)

    

best.config(command=SaveEst)

l1t=ttk.Label(EditerEtudiant,text="Nom:")
l1t.grid(row=0,column=0,pady=10)
e1t=ttk.Entry(EditerEtudiant,width=40)
e1t.grid(row=0,column=1,pady=10)
l2t=ttk.Label(EditerEtudiant,text="Prenom:")
l2t.grid(row=1,column=0,pady=10)
e2t=ttk.Entry(EditerEtudiant,width=40)
e2t.grid(row=1,column=1,pady=10)
l3t=ttk.Label(EditerEtudiant,text="Niveau:")
l3t.grid(row=2,column=0,pady=10)
e3t=ttk.Entry(EditerEtudiant,width=40)
e3t.grid(row=2,column=1,pady=10)


#dans frame SupprimerEtudiant
bes=ttk.Button(SupprimerEtudiant,text="<-- Back")
bes.grid(row=5,column=0,pady=10,padx=10)
def backes():
    raise_frame(Etudiant)
bes.config(command=backes)

bees=ttk.Button(SupprimerEtudiant,text="Supprimer")
bees.grid(row=5,column=3,pady=10,padx=10)

l1sp=ttk.Label(SupprimerEtudiant,text="ID etudiant:")
l1sp.grid(row=0,column=0,pady=10)
e1sp=ttk.Entry(SupprimerEtudiant,width=40)
e1sp.grid(row=0,column=1,pady=10)

def SeEs():
    i=e1sp.get()
    s=db.execute("Select id from Etudiant where id={}".format(i))
    row=s.fetchone()
    
    if(row):
        query="DELETE FROM Etudiant WHERE id={}"
        db.execute(query.format(i))
        db.commit()
        e1sp.delete(0,END)
        messagebox.showinfo(title="operation", message="Etudiant supprimé")
    else:
        messagebox.showinfo(title="error", message="Etudiant n'existe pas")
bees.config(command=SeEs)

#dans frame ConsulterNoteEtudiant
bbes=ttk.Button(ConsulterNoteEtudiant,text="<-- Back")
bbes.grid(row=5,column=0,pady=10,padx=10)
def bacckes():
    raise_frame(Etudiant)
bbes.config(command=bacckes)

bcon=ttk.Button(ConsulterNoteEtudiant,text="Consulter Notes")
bcon.grid(row=5,column=3,pady=10,padx=10)        

l1sep=ttk.Label(ConsulterNoteEtudiant,text="ID etudiant:")
l1sep.grid(row=0,column=0,pady=10)
e1con=ttk.Entry(ConsulterNoteEtudiant,width=40)
e1con.grid(row=0,column=1,pady=10)
def Scon():
    scon=db.execute("select * from Note where ide={}".format(e1con.get()))
    sv=scon.fetchall()    
    e1con.delete(0,END)
    s=""
    for i in sv:
        s=s+i['code']+" : {}".format(i['note'])+"\n"
    messagebox.showinfo(title="Notes Etudiant", message="{}".format(s))

bcon.config(command=Scon)


#dans frame CalculerNoteEtudiant
bbbes=ttk.Button(CalculerNoteEtudiant,text="<-- Back")
bbbes.grid(row=5,column=0,pady=10,padx=10)
def bacbckes():
    raise_frame(Etudiant)
bbbes.config(command=bacbckes)

beeesc=ttk.Button(CalculerNoteEtudiant,text="Calculer Moyen")
beeesc.grid(row=5,column=3,pady=10,padx=10)
def getID():
    return e1sepcc.get()
def getx(x):
    return x['ide']
def SecceEs(): 
    conn=db.execute("select * from Note")
    vv=conn.fetchall()
    l=[]
    for i in vv:
        l.append(i)

    print(l)
    result = list(filter(lambda x:(int(getID())==int(getx(x))), l))  
    lp=[]
    for a in result:
        lp.append(int(a['note']))
    sum=reduce(lambda x,y:x+y,lp)
    
    ms=lp.__len__()
    moy=float(sum)/float(ms)
    print(moy)
    e1sepcc.delete(0,END)
    messagebox.showinfo(title="Moyen Etudiant", message="Moyen= {} ".format(moy))


    
beeesc.config(command=SecceEs)

l1sepcc=ttk.Label(CalculerNoteEtudiant,text="ID etudiant:")
l1sepcc.grid(row=0,column=0,pady=10)
e1sepcc=ttk.Entry(CalculerNoteEtudiant,width=40)
e1sepcc.grid(row=0,column=1,pady=10)


#dans frame Cours
bc=ttk.Button(Cours,text="<-- Back")
bc.grid(row=5,column=0)
def backC():
    raise_frame(Home)
bc.config(command=backC)

b1c=ttk.Button(Cours,text="Ajouter Cours")
b1c.grid(row=0,column=0,ipadx=10,ipady=10,padx=20,pady=20)
def b1cClick():
    raise_frame(AjouterCours)
b1c.config(command=b1cClick)


b2c=ttk.Button(Cours,text="Supprimer Cours")
b2c.grid(row=0,column=1,ipadx=10,ipady=10,padx=20,pady=20)
def b2cClick():
    raise_frame(SupprimerCours)
b2c.config(command=b2cClick)
 
b3c=ttk.Button(Cours,text="Editer Cours")
b3c.grid(row=0,column=2,ipadx=10,ipady=10,padx=20,pady=20)
def b3cClick():
    raise_frame(EditerCours1)    
b3c.config(command=b3cClick)

b4c=ttk.Button(Cours,text="Calculer la moyenne \n      d’une classe")
b4c.grid(row=3,column=0,ipadx=10,ipady=10,padx=20,pady=20,columnspa=2)
def b4cClick():
    raise_frame(CalculerNoteClasse)
b4c.config(command=b4cClick)

b5c=ttk.Button(Cours,text="Consulter les notes \n      d’une classe")
b5c.grid(row=3,column=1,ipadx=10,ipady=10,padx=20,pady=20,columnspa=2)
def b5cClick():
    raise_frame(ConsulterNoteClasse)
b5c.config(command=b5cClick)

#dans frame AjouterCours
bac=ttk.Button(AjouterCours,text="<-- Back")
bac.grid(row=5,column=0,pady=10,padx=10)
def backac():
    raise_frame(Cours)
bac.config(command=backac)


l1a=ttk.Label(AjouterCours,text="Code:")
l1a.grid(row=0,column=0,pady=10)
ent1=ttk.Entry(AjouterCours,width=40)
ent1.grid(row=0,column=1,columnspa=3,pady=10)
l2a=ttk.Label(AjouterCours,text="Intitulé:")
l2a.grid(row=1,column=0,pady=10)
ent2=ttk.Entry(AjouterCours,width=40)
ent2.grid(row=1,column=1,columnspa=3,pady=10)
l3a=ttk.Label(AjouterCours,text="Niveau:")
l3a.grid(row=2,column=0,pady=10)
SpanC=StringVar()
ent3=ttk.Radiobutton(AjouterCours,text="A",variable=SpanC,value="A")
ent3.grid(row=2,column=1)
ent4=ttk.Radiobutton(AjouterCours,text="B",variable=SpanC,value="B")
ent4.grid(row=2,column=2)
ent5=ttk.Radiobutton(AjouterCours,text="C",variable=SpanC,value="C")
ent5.grid(row=2,column=3)

bcs=ttk.Button(AjouterCours,text="Sauvegarder")
bcs.grid(row=5,column=4,pady=10,padx=10)
def SaveeCs():
    cd=ent1.get()
    intitule=ent2.get()
    niveau=SpanC.get()
    db.execute("insert into Cours(code,intitule,niveau) values(?,?,?)",(cd,intitule,niveau))
    db.commit()
    ent1.delete(0,END)
    ent2.delete(0,END)
    
bcs.config(command=SaveeCs)

#dans EditerCours1
beschv=ttk.Button(EditerCours1,text="<-- Back")
beschv.grid(row=5,column=0,pady=10,padx=10)
def backeschv():
    raise_frame(Cours)
beschv.config(command=backeschv)

bescc=ttk.Button(EditerCours1,text="Editer")
bescc.grid(row=5,column=3,pady=10,padx=10)
def SecEs():
    
    saha=aha.get()
    saha="'"+saha+"'"
    print(saha)
    pah=db.execute("Select * from Cours where code={}".format(saha))
    rowpah=pah.fetchone()
    
    if(rowpah):
        e1a.insert(0,saha)
        e2a.insert(0,rowpah['intitule'])
        e3a.insert(0,rowpah['niveau'])
        raise_frame(EditerCours)

        
    else:
        messagebox.showinfo(title="error", message="Cours n'existe pas")
bescc.config(command=SecEs)

lah=ttk.Label(EditerCours1,text="Code cours:")
lah.grid(row=0,column=0,pady=10)
aha=ttk.Entry(EditerCours1,width=40)
aha.grid(row=0,column=1,pady=10)





#dans frame EditerCours
bact=ttk.Button(EditerCours,text="<-- Back")
bact.grid(row=5,column=0,pady=10,padx=10)
def backact():
    e1a.delete(0,END)
    e2a.delete(0,END)
    e3a.delete(0,END)
    raise_frame(EditerCours1)
bact.config(command=backact)

bcst=ttk.Button(EditerCours,text="Sauvegarder")
bcst.grid(row=5,column=3,pady=10,padx=10)
def SavetCs():
    popa=aha.get()    
    sa2=e2a.get()
    sa3=e3a.get()

    db.execute("UPDATE Cours SET  intitule=(?), niveau=(?) WHERE code=(?) ",(sa2, sa3, popa))
    db.commit()
    messagebox.showinfo(title="error", message="cours edité")
    e1a.delete(0,END)
    e2a.delete(0,END)
    e3a.delete(0,END)
    raise_frame(EditerCours1)

bcst.config(command=SavetCs)

l1a=ttk.Label(EditerCours,text="Code:")
l1a.grid(row=0,column=0,pady=10)
e1a=ttk.Entry(EditerCours,state='disabled',width=40)
e1a.grid(row=0,column=1,pady=10)
l2a=ttk.Label(EditerCours,text="Intitulé1:")
l2a.grid(row=1,column=0,pady=10)
e2a=ttk.Entry(EditerCours,width=40)
e2a.grid(row=1,column=1,pady=10)
l3a=ttk.Label(EditerCours,text="Niveau:")
l3a.grid(row=2,column=0,pady=10)
e3a=ttk.Entry(EditerCours,width=40)
e3a.grid(row=2,column=1,pady=10)


#dans frame SupprimerCours
besc=ttk.Button(SupprimerCours,text="<-- Back")
besc.grid(row=5,column=0,pady=10,padx=10)
def backesc():
    raise_frame(Cours)
besc.config(command=backesc)

bescc=ttk.Button(SupprimerCours,text="Supprimer")
bescc.grid(row=5,column=3,pady=10,padx=10)
def bSecEs():
    
    s=e1spc.get()
    s="'"+s+"'"
    print(s)
    p=db.execute("Select code from Cours where code={}".format(s))
    rowp=p.fetchone()
    print(rowp)
    if(rowp):
        qp="DELETE FROM Cours WHERE code={}"
        db.execute(qp.format(s))
        db.commit()
        e1spc.delete(0,END)
        messagebox.showinfo(title="operation", message="Cours supprimé")
    else:
        messagebox.showinfo(title="error", message="Cours n'existe pas")
bescc.config(command=bSecEs)

l1spc=ttk.Label(SupprimerCours,text="Code cours:")
l1spc.grid(row=0,column=0,pady=10)
e1spc=ttk.Entry(SupprimerCours,width=40)
e1spc.grid(row=0,column=1,pady=10)


#dans frame ConsulterNoteClasse
bbesm=ttk.Button(ConsulterNoteClasse,text="<-- Back")
bbesm.grid(row=5,column=0,pady=10,padx=10)
def bacckesm():
    raise_frame(Cours)
bbesm.config(command=bacckesm)

bms=ttk.Button(ConsulterNoteClasse,text="Consulter Notes")
bms.grid(row=5,column=3,pady=10,padx=10)
def tostring(x):
        s=""
        p=str(x)
        s=s+p
        return s

def Sms():
    coo=db.execute("select * from Note")
    vov=coo.fetchall()
    l=[]
    for i in vov:
        l.append(i)
#    ----------------------------

    res = list(filter(lambda x:(tostring(e1sepx.get()))==(tostring(x['code'])), l))
    if(res):
        d=""
        for o in res:
            f=db.execute("select prenom,nom from Etudiant where id={}".format(o['ide']))
            rowf=f.fetchone()
            h=str(o['note'])
            nom=str(rowf['nom'])
            prenom=str(rowf['prenom'])
            d=d+prenom+" "+nom +" : "+h+"\n"
        messagebox.showinfo(title="Note {}".format(tostring(e1sepx.get())), message="{}".format(d))
        e1sepx.delete(0,END)

    else:
        messagebox.showinfo(title="error", message="Cours n'existe pas")

    

bms.config(command=Sms)

l1sepx=ttk.Label(ConsulterNoteClasse,text="Code Cours:")
l1sepx.grid(row=0,column=0,pady=10)
e1sepx=ttk.Entry(ConsulterNoteClasse,width=40)
e1sepx.grid(row=0,column=1,pady=10)

#dans frame CalculerNoteClasse
bbbesm=ttk.Button(CalculerNoteClasse,text="<-- Back")
bbbesm.grid(row=5,column=0,pady=10,padx=10)
def bamcbckes():
    raise_frame(Cours)
bbbesm.config(command=bamcbckes)

beeescm=ttk.Button(CalculerNoteClasse,text="Calculer Moyen")
beeescm.grid(row=5,column=3,pady=10,padx=10)
def SecmceEs():

    coo=db.execute("select * from Note")
    vov=coo.fetchall()
    l=[]
    for i in vov:
        l.append(i)
    

    res = list(filter(lambda x:(tostring(e1sepccm.get()))==(tostring(x['code'])), l))
    if(res):
        lp=[]
        for a in res:
            lp.append(int(a['note']))
        sum=reduce(lambda x,y:x+y,lp)
        
        ms=lp.__len__()
        moy=float(sum)/float(ms)
        print(moy)
        e1sepcc.delete(0,END)
        messagebox.showinfo(title="Moyen Classe", message="Moyen classe = {} ".format(moy))
    else:
        messagebox.showinfo(title="error", message="Cours n'existe pas")

beeescm.config(command=SecmceEs)

l1sepccm=ttk.Label(CalculerNoteClasse,text="Code Cours:")
l1sepccm.grid(row=0,column=0,pady=10)
e1sepccm=ttk.Entry(CalculerNoteClasse,width=40)
e1sepccm.grid(row=0,column=1,pady=10)


        
#dans frame Note
bn=ttk.Button(Note,text="<-- Back")
bn.grid(row=5,column=0)
def backn():
    raise_frame(Home)
bn.config(command=backn)

b1n=ttk.Button(Note,text="Ajouter Note")
b1n.grid(row=0,column=0,ipadx=10,ipady=10,padx=20,pady=20)
def b1nClick():
    raise_frame(AjouterNote)
b1n.config(command=b1nClick)


b2n=ttk.Button(Note,text="Supprimer Note")
b2n.grid(row=0,column=1,ipadx=10,ipady=10,padx=20,pady=20)
def b2nClick():
    raise_frame(SupprimerNote)
b2n.config(command=b2nClick)

b3n=ttk.Button(Note,text="Editer Note")
b3n.grid(row=0,column=2,ipadx=10,ipady=10,padx=20,pady=20)
def b3nClick():
    raise_frame(EditerNote1)    
b3n.config(command=b3nClick)

#dans frame AjouterNote
ban=ttk.Button(AjouterNote,text="<-- Back")
ban.grid(row=5,column=0,pady=10,padx=10)
def backan():
    raise_frame(Note)
ban.config(command=backan)

bns=ttk.Button(AjouterNote,text="Sauvegarder")
bns.grid(row=5,column=3,pady=10,padx=10)

l11n=ttk.Label(AjouterNote,text="ID etudiant:")
l11n.grid(row=0,column=0,pady=10)
e11n=ttk.Entry(AjouterNote,width=40)
e11n.grid(row=0,column=1,pady=10)
l22n=ttk.Label(AjouterNote,text="Code cours:")
l22n.grid(row=1,column=0,pady=10)
e22n=ttk.Entry(AjouterNote,width=40)
e22n.grid(row=1,column=1,pady=10)
l33n=ttk.Label(AjouterNote,text="Note:")
l33n.grid(row=2,column=0,pady=10)
e33n=ttk.Entry(AjouterNote,width=40)
e33n.grid(row=2,column=1,pady=10)

def Savenss():


    ik=e11n.get()
    sk=db.execute("Select id from Etudiant where id={}".format(ik))
    rowk=sk.fetchone()

    s=e22n.get()
    s="'"+s+"'"
    print(s)
    p=db.execute("Select code from Cours where code={}".format(s))
    rowp=p.fetchone()
    print(rowp)
    idi=e11n.get()
    print()
    print(idi)
    coden=e22n.get()
   # coden="'"+coden+"'"
    print(coden)
    notee=e33n.get()
    if(rowp and rowk):
        db.execute("insert into Note(code,ide,note) values(?,?,?)",(coden,idi,notee))
        db.commit()
        e11n.delete(0,END)
        e22n.delete(0,END)
        e33n.delete(0,END)
        messagebox.showinfo(title="operation", message="note ajoutée ")
    else:
        messagebox.showinfo(title="error", message="etudiant ou cours n'existe pas ")


bns.config(command=Savenss)


#dans frame EditerNote1
label1=StringVar()
label2=StringVar()

edn1=ttk.Button(EditerNote1,text="<-- Back")
edn1.grid(row=5,column=0,pady=10,padx=10)
def baha():
    raise_frame(Note)
edn1.config(command=baha)

ben10=ttk.Button(EditerNote1,text="Editer")
ben10.grid(row=5,column=3,pady=10,padx=10)

l1snc=ttk.Label(EditerNote1,text="Code cours:")
l1snc.grid(row=0,column=0,pady=10)
j=ttk.Entry(EditerNote1,width=40)
j.grid(row=0,column=1,pady=10)
l2snc=ttk.Label(EditerNote1,text="ID etudiant:")
l2snc.grid(row=1,column=0,pady=10)
k=ttk.Entry(EditerNote1,width=40)
k.grid(row=1,column=1,pady=10)

def jk():
    coj=db.execute("select * from Note where ide={}".format(k.get()))
    voj=coj.fetchall()
    l=[]
    for i in voj:
        l.append(i)
    print(l)
    saj=j.get()
    saj="'"+saj+"'"
    
    resaj = list(filter(lambda x:(tostring(j.get()))==(tostring(x['code'])), l))
    if(resaj):
        label1.set(j.get())
        label2.set(k.get())
        print(resaj)
        e3n.insert(0,resaj[0]['note'])
        raise_frame(EditerNote)
    else:
        messagebox.showinfo(title="operation", message="note n'existe pas")
ben10.config(command=jk)

#dans frame EditerNote
bant=ttk.Button(EditerNote,text="<-- Back")
bant.grid(row=5,column=0,pady=10,padx=10)
def batckan():
    raise_frame(EditerNote1)
bant.config(command=batckan)

bnst=ttk.Button(EditerNote,text="Sauvegarder")
bnst.grid(row=5,column=3,pady=10,padx=10)
def Stavens():
    sub=k.get()
    saj=j.get()
    saj="'"+saj+"'"
    sn3=e3n.get()    

    db.execute("UPDATE Note SET  note=(?) WHERE code=(?)  ",(sn3,tostring(j.get())))
    db.commit()
    
    label1.set("")
    label2.set("")
    e3n.delete(0,END)
    messagebox.showinfo(title="operation", message="note editée ")
    raise_frame(EditerNote1)
    k.delete(0,END)
    j.delete(0,END)


bnst.config(command=Stavens)


l1n=ttk.Label(EditerNote,text="ID etudiant:")
l1n.grid(row=0,column=0,pady=10)
e1n=ttk.Label(EditerNote,width=40,textvariable=label2)
e1n.grid(row=0,column=1,pady=10)
l2n=ttk.Label(EditerNote,text="Code cours:")
l2n.grid(row=1,column=0,pady=10)
e2n=ttk.Label(EditerNote,width=40,textvariable=label1)
e2n.grid(row=1,column=1,pady=10)
l3n=ttk.Label(EditerNote,text="Note:")
l3n.grid(row=2,column=0,pady=10)
e3n=ttk.Entry(EditerNote,width=40)
e3n.grid(row=2,column=1,pady=10)


#dans frame SupprimerNote
#--------------------------------------------
bescn=ttk.Button(SupprimerNote,text="<-- Back")
bescn.grid(row=5,column=0,pady=10,padx=10)
def backescn():
    raise_frame(Note)
bescn.config(command=backescn)

ben=ttk.Button(SupprimerNote,text="Supprimer")
ben.grid(row=5,column=3,pady=10,padx=10)

l1snc=ttk.Label(SupprimerNote,text="Code cours:")
l1snc.grid(row=0,column=0,pady=10)
e1snc=ttk.Entry(SupprimerNote,width=40)
e1snc.grid(row=0,column=1,pady=10)
l2snc=ttk.Label(SupprimerNote,text="ID etudiant:")
l2snc.grid(row=1,column=0,pady=10)
e2snc=ttk.Entry(SupprimerNote,width=40)
e2snc.grid(row=1,column=1,pady=10)

def Smn():
    coo=db.execute("select * from Note where ide={}".format(e2snc.get()))
    vov=coo.fetchall()
    l=[]
    for i in vov:
        l.append(i)
    san=e1snc.get()
    san="'"+san+"'"
    
    res = list(filter(lambda x:(tostring(e1snc.get()))==(tostring(x['code'])), l))
    for i in res:
        print(i['note'],i['code'],i['ide'])
        db.execute("delete from Note where code={} and ide={}".format(san,e2snc.get()))
        db.commit()
    if(res):
         messagebox.showinfo(title="operation", message="note supprimé ")
    if(res==[]):
        messagebox.showinfo(title="operation", message="note n'existe pas")


ben.config(command=Smn)


raise_frame(Home)

root.mainloop()

