#Név/Évfolyam/Átlag

class Diak:
    def __init__(self,nev,evfolyam,atlag:str):
        self.nev=nev
        self.evfolyam=int(evfolyam)
        self.atlag=float(atlag.replace(",","."))
    def __str__(self):
        return f"{self.nev},{self.evfolyam},{self.atlag}"