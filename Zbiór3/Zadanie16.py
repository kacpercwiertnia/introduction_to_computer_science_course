import random

n = int(input("n="))

tablica = [random.randint(1,1000) for _ in range(n)]

print(tablica)

najw = 0
najm = tablica[0]
poww = False
powm = 0

for i in range(n):
  if tablica[i] > najw:
    najw = tablica[i]
    poww = False
  elif tablica[i] == najw:
    poww = True
  
  if tablica[i] > najm:
    najm = tablica[i]
    powm = False
  elif tablica[i] == najm:
    powm = True

if not poww and not powm:
  print("Są")
else:
  print("Nie są")

