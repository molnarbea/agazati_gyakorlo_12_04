from Diak import Diak
def sorokba():
    f=open("suli.txt","r",encoding="UTF8")
    f.readline()
    sorok=f.readlines()
    f.close()
    return sorok

def objektum_listaba(sorok:list[str]):
    diakok=[]
    for i in range(len(sorok)):
        adatok=sorok[i].strip().split("/")
        diak=Diak(adatok[0],adatok[1],adatok[2])
        diakok.append(diak)
    return diakok
def lista_kiiras(diakok):
    for i in range(len(diakok)):
        print(diakok[i])

def atlag(diakok):
    ossz=0
    for i in range(len(diakok)):
        ossz+=diakok[i].atlag
    atlag=ossz/len(diakok)
    print(f"Az osztály átlaga: {atlag:.2f}")

def teljes():
    sorok=sorokba()
    diakok=objektum_listaba(sorok)
    #print(diakok)
    lista_kiiras(diakok)
    print(len(diakok))
    atlag(diakok)
    