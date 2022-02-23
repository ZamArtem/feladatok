class fifa:
    def __init__(self,sor):
        csapat, helyezes, valtozas, pontszam = sor.strip().split(";")
        self.csapat = csapat
        self.helyezes = int(helyezes)
        self.valtozas = int(valtozas)
        self.pontszam = int(pontszam)
       

with open("fifa.txt", "r",encoding="UTF 8") as f:
    cimsor = f.readline()
    lista = [fifa(sor) for sor in f]
#3.Feladat
csapat = [sor.csapat for sor in lista]
print(f"3. feladat: A világranglistán {len(csapat)} csapat szerepel")
#4.Feladat
pontszam = [sor.pontszam for sor in lista]
print(f"4. feladat: A csapatok átlagos pontszáma: {sum(pontszam) / len(pontszam)}")
#5.Feladat
print("5' feladat: A legtöbbet javító csapat:")
valtozas = [sor.valtozas for sor in lista]

print(max(valtozas))
print(f"""        Helyezés:""")
print(f"""        Csapat:""")
print(f"""        Pantszám:""")

