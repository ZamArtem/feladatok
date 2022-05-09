''' 
1. Hány szám van a listában?
Készíts függvényt lista_elemek_szama() néven,  amely visszatér egy lista elemeinek a számával 

2. Melyik a legkisebb szám a listában?
Készíts függvényt legkisebb() néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.

3. Mennyi a lista számainak összege?
Készíts függvényt osszeg() néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.

4. Mennyi a lista számainak szorzata?
Készíts függvényt szorzat() néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával.

5. Melyik a legnagobb szám a listában?
Készíts függvényt legnagyobb() néven,  amely visszatér egy számokat tartalmazó lista legnagyobb számával.

6. Melyik a legelső szám a listában?
Készíts függvényt legelso() néven,  amely visszatér egy számokat tartalmazó lista legelso számával.

7. Melyik a utolso szám a listában?
Készíts függvényt utolso() néven,  amely visszatér egy számokat tartalmazó lista utolso számával.

8. Mennyi a páros számok száma a listában?
Készíts függvényt parosok_szama() néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával.

9. Első kettő.
Készíts függvényt elso_ketto() néven,  amely visszatér egy számokat tartalmazó lista első két számával mint listával.

10. Első és utolsó
Készíts függvényt elso_utolso() néven,  amely visszatér egy számokat tartalmazó lista első ás utolsó számával mint listával.
'''



def lista_elemek_szama(listas):
  return len(listas)

def legkisebb(listas):
  return min(listas)

def osszeg(listas):
  return sum(listas)
  
def szorzat(listas):
  x = 1
  for sor in listas:
    x = sor * x
  return x
  
def legnagyobb(listas):
  return max(listas)

def legelso(listas):
  return listas[0]

def utolso(listas):
  return listas[-1]

def parosok_szama(listas):
  return len([sor for sor in listas if sor % 2 == 0])

def elso_ketto(listas):
  x = []
  for sor in listas:
    x.append(sor)
    if len(x) == 2:
      break
  return x
  
def elso_utolso(listas):
  x = []
  x.append(listas[0])
  x.append(listas[-1])
  return x
