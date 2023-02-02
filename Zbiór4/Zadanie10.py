T = [[0,2,3,3,0],
     [1,0,3,3,0],
     [1,2,1,3,0],
     [1,2,3,0,0],
     [1,2,3,3,0]]

def zera(T):
  for y in range(len(T)):
    kolumna = False
    wiersz = False
    for x in range(len(T)):
      if T[y][x] == 0:
        wiersz = True
      if T[x][y] == 0:
        kolumna = True
    if not kolumna or not wiersz:
      return False
  return True

print(zera(T))