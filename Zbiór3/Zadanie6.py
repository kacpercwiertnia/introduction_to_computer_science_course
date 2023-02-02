import random

n = int(input("n="))

tablica = [random.randint(1, 1000) for _ in range(n)]

print(tablica)

for i in range(n):
  czy_ok = False
  while tablica[i] > 0:
    if (tablica[i]%10)%2!=0:
      czy_ok = True
      break
    tablica[i]//=10
  if czy_ok == False:
    print("Nie wszystkie")
    break
else:
  print("Wszystkie")