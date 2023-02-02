import random
n = int(input("n="))
tab = [[random.randint(-100,100) for _ in range (n)]for _ in range (n)]

for linia in tab:
  print(linia)

kol_dod_max = 0
kol_uje_max = 0
wier_dod_min = 100000000
wier_uje_min = -10000000

suma_kol = 0
suma_wier = 0

y_dod_max = 0
y_uje_max = 0

x_dod_min = 0
x_uje_min = 0

for y in range(n):
  for x in range(n):
    suma_kol += tab[x][y]
    suma_wier += tab[y][x]
  if suma_kol > 0:
    if suma_kol > kol_dod_max:
      kol_dod_max = suma_kol
      y_dod_max = y
  else:
    if suma_kol < kol_uje_max:
      kol_uje_max = suma_kol
      y_uje_max = y
  if suma_wier > 0:
    if suma_wier < wier_dod_min:
      wier_dod_min = suma_wier
      x_dod_min = y
  else:
    if suma_wier > wier_uje_min:
      wier_uje_min = suma_wier
      x_uje_min = y
  suma_kol = 0
  suma_wier = 0

if kol_dod_max/wier_dod_min > kol_uje_max/wier_uje_min:
  print(y_dod_max, x_dod_min)
else:
  print(y_uje_max, x_uje_min)