class Epulet:
    def __init__(self,nev,varos,orszag,magassag:int,emeletek,ev):
        self.nev=nev
        self.varos=varos
        self.orszag=orszag
        self.magassag=magassag
        self.emeletek=emeletek
        self.ev=ev
    def __str__(self):
        return f"{ self.nev},{self.varos},{self.orszag},{self.magassag},{self.emeletek},{self.ev}"