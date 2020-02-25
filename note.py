class Note:

    def __init__(self,ide,codec,note):
        self.ide= ide
        self.codec=codec
        self.note=note

def AjouterNote(ide,codec,note):
    n=Note(ide,codec,note)
    print(n.note)

AjouterNote(12,10,20)