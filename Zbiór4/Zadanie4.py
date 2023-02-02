import random

n = int(input("n="))

tablica = [[ random.randint(1,100) for _ in range(n)] for _ in range(n)]

for linia in tablica:
  print(linia)

suma_x_max = 0
suma_y_min = 1000000

x_max = 0
y_min = 0

for y in range(n):
  suma_y = 0
  suma_x = 0
  for x in range(n):
    suma_y += tablica[y][x]
    suma_x += tablica[x][y]
  if suma_x > suma_x_max:
    suma_x_max = suma_x
    x_max = y
  if suma_y < suma_y_min:
    suma_y_min = suma_y
    y_min = y

print(x_max, y_min)

