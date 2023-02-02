n = int(input("n="))

calk = 1//1 + 1//1
mianownik = 2
dzies = [0 for _ in range(n)]
rozw_dziel = [0 for _ in range(n)]
dzies[0] = 5
rozw_dziel[0] = 5

while max(rozw_dziel) != 0:
  licznik = 0
  nast = 0
  mianownik+=1
  for x in range(n):
    licznik *= 10
    licznik += rozw_dziel[x]
    calkowite = licznik//mianownik
    licznik = licznik - calkowite*mianownik
    rozw_dziel[x] = calkowite
  for x in range(n-1,-1,-1):
    suma = rozw_dziel[x] + nast + dzies[x]
    if suma >= 10:
      nast = suma // 10
      dzies[x] = suma - nast*10
    else:
      dzies[x] = suma
      nast = 0

print(calk,end=".")
for x in dzies:
  print(x,end="")