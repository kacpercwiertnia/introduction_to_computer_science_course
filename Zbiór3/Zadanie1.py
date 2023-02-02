n = int(input("n="))
tablica = [[0 for _ in range(n)] for _ in range(n)]

start = 0
i = 1
warunek = n*n

while i <= warunek:
  x = start
  y = start
  while x < n - start:
    tablica[y][x] = i
    i+=1
    x+=1
  x -= 1
  y += 1
  while y < n - start:
    tablica[y][x] = i
    i+=1
    y+=1
  y -= 1
  x -= 1
  while x > start - 1:
    tablica[y][x] = i
    i+=1
    x-=1
  x = start
  y -= 1
  while y > start:
    tablica[y][x] = i
    i+=1
    y-=1
  y += 2
  start += 1

for linia in tablica:
  print(linia)