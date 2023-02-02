import random

n = int(input("n="))

tablica = [random.randint(1,100) for _ in range(n)]

print(tablica)

dl = 2
dl_max = 1

if n > 1:
  r = tablica[0] - tablica[1]
  for i in range(1,n-1):
    if r == tablica[i] - tablica[i+1]:
      dl+=1
    else:
      r = tablica[i] - tablica[i+1]
      if dl > dl_max:
        dl_max = dl
      dl = 2

print(dl_max)