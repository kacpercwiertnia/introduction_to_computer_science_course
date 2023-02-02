n = int(input("n="))

roznica = 0
roznica_naj = n
dzielnik = 1
dzielnik_naj = 0

while dzielnik*dzielnik < n:
  if n%dzielnik==0:
    roznica = n//dzielnik - dzielnik
    if roznica < roznica_naj:
      roznica_naj = roznica
      dzielnik_naj = dzielnik
  dzielnik+=1

print(dzielnik_naj, n//dzielnik_naj)