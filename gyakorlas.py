def feladat1():
    szam = 0
    while szam < 150:
        print(szam, end=";")
        szam += 2
    print(szam)


def feladat2():
    szamok = 0
    bekertszamok = 0
    while szamok < 10545:
        szam = float(input("Adj meg egy számot!: "))
        if szam % 3 == 0:
            bekertszamok += 1
        szamok += 1
    print("A hárommal osztható számok száma: " + str(bekertszamok))


def feladat3():
    szam = 0
    bekert = int(input("Adj meg egy számot!: "))
    szam = szam + bekert
    while szam % 10 != 0:
        bekert = int(input("Adj meg egy számot!: "))
        szam = szam + bekert
    print("Gratulálunk nyertél!")


def feladat4a():
    x = float(input("Adj meg egy számot!: "))
    while not (x % 2 == 0 and 10 <= x <= 98):
        x = float(input("Adj meg egy számot!: "))
    print("A szám osztható kettővel!")


def feladat4b():
    x = float(input("Adj meg egy számot!: "))
    x = abs(x)
    while not (x % 2 == 0 and 10 <= x <= 98):
        x = float(input("Adj meg egy számot!: "))
        x = abs(x)
    print("A szám osztható kettővel!")


def feladat5():
    x = int(input("Adj meg egy számot!: "))
    while not (x > 0 and x % 2 == 0):
        x = int(input("Adj meg egy számot!: "))
    print("A számod páratlan és nagyobb mint 0!")


def feladat6():
    x = int(input("Adj meg egy számot!: "))
    while not ((x ** 0.5) % 1 == 0 or x % 3 == 0):
        x = int(input("Adj meg egy számot!: "))
    print("A szám oszható hárommal vagy négyzetszám!")


def feladat7():
    x = int(input("Adj meg egy számot!: "))
    y = int(input("Adj meg még egy számot!: "))
    z = int(input("Adj meg egy harmadik számot!: "))

    while not (x + y > z and x + z > y and y + z > x):
        x = int(input("Adj meg egy számot!: "))
        y = int(input("Adj meg még egy számot!: "))
        z = int(input("Adj meg egy harmadik számot!: "))
    print("szerkeszthető háromszög!")


def feladat8():
    szo = str(input("Írj be min. három karaktert!: "))
    while not (len(szo) >= 3):
        szo = str(input("Írj be min. három karaktert!: "))
    print(szo.upper())


def feladat9():
    szo = str(input("Írj be négy karaktert kisbetűvel!: "))
    while not (len(szo) == 4 and szo.islower()):
        szo = str(input("Írj be négy karaktert kisbetűvel!: "))
    print("Gratulálunk nyertél!")


def feladat10():
    y = 0
    z = 0
    x = int(input("Adj meg egy számot!: "))
    y += x
    while not x == 0:
        x = int(input("Adj meg egy számot!: "))
        y += x
        z += 1
    atlag = y / z
    print("A számok átlaga: ", "{:.3}".format(atlag))


def feladat11():
    y = 0
    z = 0
    x = int(input("Adj meg egy számot!: "))
    while not (x == 0):
        while not (x > 0):
            x = int(input("Adj meg egy számot!: "))
        y += x
        z += 1
        x = int(input("Adj meg egy számot!: "))

    atlag = y / z
    print("A számok átlaga: ", "{:.3}".format(atlag))


def feladat12():
    letszam = int(input("Add meg a létszámot!: "))
    szintido = 0
    eredmenyek = 0
    serultek = 0
    while not eredmenyek == letszam:
        x = int(input("Add meg a szintidőt másodpercben: "))
        if x > 0:
            eredmenyek += 1
            szintido += x
        elif x == 0:
            eredmenyek += 1
            serultek += 1
        else:
            print("Helytelen adat!")

    vegzett = eredmenyek - serultek
    szazalek = vegzett / letszam * 100
    atlagered = szintido / vegzett
    print(vegzett, "sikeres befutó", szazalek, "%-a ért be a veresenyzőknek", "átlag teljesítményük:", atlagered, "mp")


def feladat12b():
    letszam = int(input("Add meg a létszámot!: "))
    if letszam < 0:
        print("Hibás adat!")
        letszam = int(input("Add meg a létszámot!: "))
    szintido = 0
    eredmenyek = 0
    serultek = 0
    monoton = True
    elozo = 0
    while not eredmenyek == letszam:
        x = int(input("Add meg a szintidőt másodpercben: "))
        if x > 0:
            eredmenyek += 1
            szintido += x
            if x > elozo:
                print("A szintidő nagyobb mint az előző érték.")
            else:
                monoton = False
            elozo = x
        elif x == 0:
            eredmenyek += 1
            serultek += 1
            elozo = x
        else:
            print("Helytelen adat!")

    vegzett = eredmenyek - serultek
    szazalek = vegzett / letszam * 100
    atlagered = szintido / vegzett
    if monoton:
        print("A számsor szingorúan monoton")
        print(vegzett, "sikeres befutó", szazalek, "%-a ért be a veresenyzőknek", "átlag teljesítményük:", atlagered,
              "mp")
    else:
        print("A számsor nem szigorúan monoton!")
        print(vegzett, "sikeres befutó", szazalek, "%-a ért be a veresenyzőknek", "átlag teljesítményük:", atlagered,
              "mp")
