def suma_dzielnikow(a):
  suma = 1
  dzielniki = 2

  while dzielniki**2<a:
    if a%dzielniki==0:
      suma+=dzielniki
      suma+=a/dzielniki
    dzielniki+=1
  if dzielniki*dzielniki==a:
    suma+=dzielniki
  return suma

for a in range(1000001):
  b = suma_dzielnikow(a)
  if a == suma_dzielnikow(b) and a>b:
      print(a,b)