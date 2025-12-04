def feladat_1():
    print("1/A")
    nev=input("\tJátékos neve: ")
    szerep=input("\tSzerepkör: ")
    print("1/B")
    if szerep=="varázsló":
        print(f"\tÜdvözlünk {nev}, 2 életed van!")
    elif szerep=="harcos":
        print(f"\tÜdvözlünk {nev}, 10 életed van!")
    else:
        print(f"\tÜdvözlünk {nev}, 8 életed van!")