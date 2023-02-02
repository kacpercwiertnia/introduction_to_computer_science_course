import random

n = int(input("n="))

tablica = [random.randint(1,100) for _ in range(n)]

print(tablica)

dl = 1
dl_max = 1

if len(tablica) > 1:
  for i in range(n-1):
    if tablica[i] < tablica[i+1]:
      dl+=1
    else:
      if dl > dl_max:
        dl_max = dl
      dl = 1

print(dl_max)