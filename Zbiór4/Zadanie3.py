import random

n = int(input("n="))

tablica = [[ random.randint(1,100) for _ in range(n)] for _ in range(n)]

for linia in tablica:
  print(linia)

for linia in tablica:
  for liczba in linia:
    while liczba > 0:
      if (liczba%10)%2 == 0:
        break
      liczba//=10
    else:
      break
  else:
    print("Jest taki wiersz")
    break
else:
  print("Nie ma takiego wiersza")