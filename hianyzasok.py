class hianyzas:
    def __init__(self,sor):
        sor = sor.strip().split(";")
        self.nev = str(sor[0])
        self.osztaly = sor[1]
        self.elso = int(sor[2])
        self.utolso = int(sor[3])
        self.mulasztas = int(sor[4])
with open("szeptember.txt",encoding="UTF 8") as f:
    lista = [hianyzas(sor) for sor in f]
#2.Feladat
tanulok =[sor.nev for sor in lista]
print(tanulok)
mulasztas = [sor.mulasztas for sor in lista]
print(f"""2. feladat
      Összes mulasztott órák száma:{sum(mulasztas)} óra.
  """)
#3.Feladat
nap = int(input("""3.Feladat 
      Aggyon meg egy számot 1 és 30 között: """))
tanulo = input("""      Aggyon egy tanúlo nevet: """)
#4.Feladat
print("4.Feladat")
if tanulo in tanulok:
    print("""       A tanuló hiányzott szeptemberben""")
else:
    print("""       A tanuló nem hiányzott szeptemberben""")
#5.Feladat
