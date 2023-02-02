import random

tablica = [random.randint(1,1000) for _ in range(100)]

a = 1
b = 1

print(tablica)

pierwsza = False

while b-1 < 100:
  dzielnik = 2
  zlozone = False
  while dzielnik*dzielnik < tablica[b-1]:
    if tablica[b]%dzielnik == 0:
      zlozone = True
      break
    dzielnik+=1
  else:
    break

  if pierwsza == False:
    for i in range(a,b-1):
      dzielnik = 2
      while dzielnik*dzielnik < tablica[i]:
        if tablica[i]%dzielnik == 0:
          break
        dzielnik+=1
      else:
        pierwsza = True
        break

  tmp = b
  b = a+b
  a = tmp

if zlozone and pierwsza:
  print("Są")
else:
  print("Nie są")