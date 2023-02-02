import random

n = int(input("n="))

tablica = [random.randint(1,1000) for _ in range(n)]

print(tablica)

for i in range(n):
  istnieje = True
  while tablica[i] > 0:
    if (tablica[i]%10)%2==0:
      istnieje = False
      break
    tablica[i]//=10
  if istnieje == True:
    print("Istnieje")
    break
else:
  print("Nie istnieje")