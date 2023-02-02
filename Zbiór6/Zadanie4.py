def skoczek(T, n, x = 0, y = 0):
  T[y][x] = 1
  ok = False
  if y + 2 < n and x - 1 > -1:
    if T[y+2][x-1] == 0:
      skoczek(T, n, x-1, y+2)
      ok = True
  if y + 2 < n and x + 1 < n:
    if T[y+2][x+1] == 0:
      skoczek(T, n, x+1, y+2)
      ok = True
  if y + 1 < n and x + 2 < n:
    if T[y+1][x+2] == 0:
      skoczek(T, n, x+2, y+1)
      ok = True
  if y - 1 > -1 and x + 2 < n:
    if T[y-1][x+2] == 0:
      skoczek(T, n, x+2, y-1)
      ok = True
  if y - 2 > -1 and x - 1 > -1:
    if T[y-2][x-1] == 0:
      skoczek(T, n, x-1, y-2)
      ok = True
  if y - 2 > -1 and x + 1 < n:
    if T[y-2][x+1] == 0:
      skoczek(T, n, x+1, y-2)
      ok = True
  if y + 1 < n and x - 2 > -1:
    if T[y+1][x-2] == 0:
      skoczek(T, n, x-2, y+1)
      ok = True
  if y - 1 > -1 and x - 2 > -1:
    if T[y-1][x-2] == 0:
      skoczek(T, n, x-2, y-1)
      ok = True
  if not ok:
    return 

n = int(input("n="))

T = [[0 for _ in range(n)] for _ in range(n)]
skoczek(T,n)

for wiersz in T:
  print(wiersz)