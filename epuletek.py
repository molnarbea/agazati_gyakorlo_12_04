from Epulet import Epulet
epulet_lista=[]
def feladat_3():
    f=open("epulet.txt","r",encoding="UTF-8")
    f.readline()
    szoveg=f.readlines()    
    f.close()

    i=0
    while i<len(szoveg):
        sor=szoveg[i].strip().split("$")
        epulet=Epulet(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5])
        epulet_lista.append(epulet)
        i+=1
    return epulet_lista

def epuletek_szama(lista):
    i=0
    while i<len(lista):
        i+=1
    print("3/A,B")
    print(f"\tAz épületek száma: {i}")

def magasabb_555(lista):
    i=0
    magasabb=0
    while i<len(lista):
        if lista[i].magassag>str(555/3.280839895):
            magasabb+=1
        i+=1
    print("3/C")
    print(f"\tAz 555 lábnál magasabb épületek száma: {magasabb}.")

def oregebb(lista):
    i=0
    orszag=""
    oregebb=2025
    while i<len(lista):
        if lista[i].ev < str(oregebb):
            oregebb=lista[i].ev
            orszag=lista[i].orszag
        i+=1
    print("3/D")
    print(f"\tA legöregebb épület országa: {orszag}.")