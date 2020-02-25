class Cours:
    class_counter= 0
    def __init__(self,code,intitule,niveau):
        self.code= code
        self.intitule=intitule
        self.niveau=niveau
        self.id= Cours.class_counter
        Cours.class_counter += 1

c=Cours("utc503","blblbl","B")
print(c.id,c.code)