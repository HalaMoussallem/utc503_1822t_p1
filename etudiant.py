class Etudiant:
    class_counter= 0
    def __init__(self,nom,prenom,niveau):
        self.nom= nom
        self.prenom=prenom
        self.niveau=niveau
        self.id= Etudiant.class_counter
        Etudiant.class_counter += 1

e=Etudiant("hala","moussallem","B")
print(e.id)

e1=Etudiant("hala","moussallem","B")
print(e1.id)
