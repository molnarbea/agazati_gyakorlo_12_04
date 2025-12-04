import random

def feladat_2():
    lista=[]
    sorozat=""
    i=0
    while len(lista) < 7:
        szam=random.randint(0,1)
        lista.append(szam)
    while len(lista) > i:
        if lista[i] == 0:
            sorozat+="írás"
        else:
            sorozat+="fej"
        if i!=6:
            sorozat+="-"
        i+=1
    print("2/A,B,C")
    print(f"\t{sorozat}")
    return lista

def fejek_szama(lista):
    i=0
    fej_db=0
    while len(lista)>i:
        if lista[i]==1:
            fej_db+=1
        i+=1
    return fej_db

def konzol_kiir(fej_db):
    print("2/D,E")
    print(f"\tA fejek száma: {fej_db}.")

def file_kiir(fej_db):
    f=open("fejek.txt","w",encoding="UTF-8")
    f.writelines("A fejek száma: ")
    f.writelines(str(fej_db))
    f.close()