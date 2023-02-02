e1 = 1
e2 = 2
silnia = 2
licznik = 3

while abs(e2-e1) > 0.000001:
  e1=e2
  e2+=(1/silnia)
  silnia*=licznik
  licznik+=1

print(e2)